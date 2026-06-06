from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any


if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from openai import OpenAI

from src.core.config import config
from src.generation.rag_answer import _build_messages, estimate_confidence
from src.retrieval.search import QueryResult, RetrievedChunk, query as retrieve_query


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GOLDEN_PATH = PROJECT_ROOT / "tests" / "eval" / "retrieval_golden_questions.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "tests" / "eval"


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def _tokens(text: str) -> list[str]:
    normalized = _strip_accents(text.lower())
    normalized = re.sub(r"[^\w\s]", " ", normalized, flags=re.UNICODE)
    stopwords = {
        "la",
        "va",
        "co",
        "cua",
        "cho",
        "trong",
        "duoc",
        "nhu",
        "the",
        "nao",
        "gi",
        "o",
        "dau",
        "mot",
        "cac",
        "ve",
        "voi",
        "de",
        "can",
        "dat",
        "nam",
    }
    return [token for token in normalized.split() if len(token) > 1 and token not in stopwords]


def _f1_overlap(left: str, right: str) -> float:
    left_counts = Counter(_tokens(left))
    right_counts = Counter(_tokens(right))
    if not left_counts or not right_counts:
        return 0.0

    overlap = sum(min(count, right_counts[token]) for token, count in left_counts.items())
    precision = overlap / sum(right_counts.values())
    recall = overlap / sum(left_counts.values())
    if precision + recall == 0:
        return 0.0
    return (2 * precision * recall) / (precision + recall)


def _first_relevant_rank(chunks: list[RetrievedChunk], expected_paths: set[str]) -> int | None:
    for index, chunk in enumerate(chunks, start=1):
        if chunk.source_path in expected_paths:
            return index
    return None


def _retrieval_metrics(result: QueryResult, expected_paths: set[str]) -> dict[str, Any]:
    chunks = result.chunks
    relevant_chunks = [chunk for chunk in chunks if chunk.source_path in expected_paths]
    first_rank = _first_relevant_rank(chunks, expected_paths)
    retrieved_expected_paths = {chunk.source_path for chunk in relevant_chunks}

    return {
        "hit_at_1": bool(first_rank and first_rank <= 1),
        "hit_at_3": bool(first_rank and first_rank <= 3),
        "hit_at_5": bool(first_rank and first_rank <= 5),
        "mrr": round(1.0 / first_rank, 4) if first_rank else 0.0,
        "first_relevant_rank": first_rank,
        "context_precision": round(len(relevant_chunks) / len(chunks), 4) if chunks else 0.0,
        # In this golden set, expected_paths usually means acceptable source paths,
        # so one matching source is treated as enough context for the question.
        "context_recall": 1.0 if relevant_chunks else 0.0,
        "expected_path_coverage": round(len(retrieved_expected_paths) / len(expected_paths), 4) if expected_paths else 0.0,
    }


def _extract_citation_numbers(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"\[S(\d+)\]", text)]


def _answer_sentences(answer: str) -> list[str]:
    parts = re.split(r"(?<=[.!?。])\s+|\n+", answer)
    return [part.strip() for part in parts if len(_tokens(part)) >= 3]


def _answer_metrics(question: str, answer: str, chunks: list[RetrievedChunk], expected_paths: set[str]) -> dict[str, Any]:
    if not answer.strip():
        return {
            "answer_relevance": None,
            "faithfulness": None,
            "citation_validity": None,
            "citation_accuracy": None,
            "citation_count": 0,
        }

    citations = _extract_citation_numbers(answer)
    valid_citations = [number for number in citations if 1 <= number <= len(chunks)]
    cited_relevant = [
        number
        for number in valid_citations
        if chunks[number - 1].source_path in expected_paths
    ]

    sentences = _answer_sentences(answer)
    sentence_scores: list[float] = []
    for sentence in sentences:
        sentence_citations = [number for number in _extract_citation_numbers(sentence) if 1 <= number <= len(chunks)]
        if not sentence_citations:
            sentence_scores.append(0.0)
            continue

        cited_context = "\n".join(chunks[number - 1].text for number in sentence_citations)
        overlap = _f1_overlap(sentence, cited_context)
        citation_support = 1.0 if sentence_citations else 0.0
        sentence_scores.append((0.45 * citation_support) + (0.55 * min(overlap / 0.35, 1.0)))

    return {
        "answer_relevance": round(_f1_overlap(question, answer), 4),
        "faithfulness": round(mean(sentence_scores), 4) if sentence_scores else 0.0,
        "citation_validity": round(len(valid_citations) / len(citations), 4) if citations else 0.0,
        "citation_accuracy": round(len(cited_relevant) / len(valid_citations), 4) if valid_citations else 0.0,
        "citation_count": len(citations),
    }


def _generate_answer(question: str, chunks: list[RetrievedChunk], model: str, temperature: float) -> str:
    if not config.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is required unless --retrieval-only is used.")

    client = OpenAI(api_key=config.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=_build_messages(question, chunks),
        temperature=temperature,
    )
    return response.choices[0].message.content or ""


def _mean_metric(cases: list[dict[str, Any]], key: str) -> float | None:
    values = [case["metrics"][key] for case in cases if case["metrics"].get(key) is not None]
    if not values:
        return None
    return round(mean(values), 4)


def _load_golden_cases(path: Path, limit: int | None = None) -> list[dict[str, Any]]:
    cases = json.loads(path.read_text(encoding="utf-8-sig"))
    if limit is not None:
        return cases[:limit]
    return cases


def _case_to_result(
    case: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    question = str(case["question"])
    expected_paths = {str(path) for path in case.get("expected_paths", [])}

    retrieval_started = time.perf_counter()
    retrieval = retrieve_query(
        question=question,
        top_k=args.top_k,
        use_rerank=not args.no_rerank,
        use_hybrid=not args.no_hybrid,
        db_path=args.db_path,
        collection_name=args.collection,
        embedding_provider=args.embedding_provider,
    )
    retrieval_seconds = time.perf_counter() - retrieval_started

    answer = ""
    generation_seconds = 0.0
    if not args.retrieval_only:
        generation_started = time.perf_counter()
        answer = _generate_answer(question, retrieval.chunks, args.model, args.temperature)
        generation_seconds = time.perf_counter() - generation_started

    metrics = {
        **_retrieval_metrics(retrieval, expected_paths),
        **_answer_metrics(question, answer, retrieval.chunks, expected_paths),
        "confidence": estimate_confidence(retrieval),
        "retrieval_latency_seconds": round(retrieval_seconds, 4),
        "generation_latency_seconds": round(generation_seconds, 4),
        "total_latency_seconds": round(retrieval_seconds + generation_seconds, 4),
    }

    return {
        "id": case.get("id"),
        "category": case.get("category"),
        "question": question,
        "expected_paths": sorted(expected_paths),
        "answer": answer,
        "metrics": metrics,
        "retrieval": {
            "method": retrieval.method,
            "top_results": [
                {
                    "rank": chunk.rank,
                    "chunk_id": chunk.chunk_id,
                    "score": round(float(chunk.score), 6),
                    "source_path": chunk.source_path,
                    "citation": chunk.citation,
                    "text_preview": chunk.text_preview,
                }
                for chunk in retrieval.chunks
            ],
        },
    }


def _build_summary(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    metric_keys = [
        "hit_at_1",
        "hit_at_3",
        "hit_at_5",
        "mrr",
        "context_precision",
        "context_recall",
        "expected_path_coverage",
        "answer_relevance",
        "faithfulness",
        "citation_validity",
        "citation_accuracy",
        "confidence",
        "retrieval_latency_seconds",
        "generation_latency_seconds",
        "total_latency_seconds",
    ]
    return {
        "case_count": len(cases),
        "top_k": args.top_k,
        "model": None if args.retrieval_only else args.model,
        "retrieval_only": args.retrieval_only,
        "use_rerank": not args.no_rerank,
        "use_hybrid": not args.no_hybrid,
        "embedding_provider": args.embedding_provider or config.EMBEDDING_PROVIDER,
        "metrics": {key: _mean_metric(cases, key) for key in metric_keys},
    }


def _write_text_report(path: Path, payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    metrics = summary["metrics"]
    lines = [
        "RAG Evaluation Report",
        f"Created at: {payload['created_at']}",
        f"Golden set: {payload['golden_path']}",
        f"Cases: {summary['case_count']}",
        f"Top-k: {summary['top_k']}",
        f"Retrieval only: {summary['retrieval_only']}",
        "",
        "Summary metrics",
    ]
    for key, value in metrics.items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "Per-case results"])
    for case in payload["cases"]:
        case_metrics = case["metrics"]
        lines.extend(
            [
                "",
                f"[{case['id']}] {case['question']}",
                f"- category: {case['category']}",
                f"- expected_paths: {', '.join(case['expected_paths'])}",
                f"- hit_at_1/hit_at_3/hit_at_5: {case_metrics['hit_at_1']} / {case_metrics['hit_at_3']} / {case_metrics['hit_at_5']}",
                f"- mrr: {case_metrics['mrr']}",
                f"- context_precision: {case_metrics['context_precision']}",
                f"- context_recall: {case_metrics['context_recall']}",
                f"- answer_relevance: {case_metrics['answer_relevance']}",
                f"- faithfulness: {case_metrics['faithfulness']}",
                f"- citation_accuracy: {case_metrics['citation_accuracy']}",
                f"- latency_seconds: {case_metrics['total_latency_seconds']}",
            ]
        )
        if case["retrieval"]["top_results"]:
            top = case["retrieval"]["top_results"][0]
            lines.append(f"- top1_source: {top['source_path']}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run RAG evaluation on a golden question set.")
    parser.add_argument("--golden", type=Path, default=DEFAULT_GOLDEN_PATH)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--prefix", default="rag_eval_results")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--model", default=config.LLM_MODEL)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--retrieval-only", action="store_true")
    parser.add_argument("--db-path", type=Path, default=Path(config.VECTOR_DB_PATH))
    parser.add_argument("--collection", default=config.CHROMA_COLLECTION_NAME)
    parser.add_argument("--embedding-provider", choices=["openai", "hash"], default=config.EMBEDDING_PROVIDER)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--no-hybrid", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    golden_cases = _load_golden_cases(args.golden, args.limit)
    case_results = [_case_to_result(case, args) for case in golden_cases]

    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "golden_path": str(args.golden),
        "summary": _build_summary(case_results, args),
        "cases": case_results,
    }

    json_path = args.out_dir / f"{args.prefix}.json"
    txt_path = args.out_dir / f"{args.prefix}.txt"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_text_report(txt_path, payload)

    print(f"Wrote JSON report: {json_path}")
    print(f"Wrote text report: {txt_path}")
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
