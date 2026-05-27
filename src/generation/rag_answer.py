from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any


if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from openai import OpenAI

from src.core.config import config
from src.retrieval.search import QueryResult, RetrievedChunk, query as retrieve_query


DEFAULT_MAX_CONTEXT_CHARS = 2600


@dataclass
class RagAnswer:
    question: str
    answer: str
    model: str
    retrieval: QueryResult
    confidence: float
    confidence_label: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "question": self.question,
            "answer": self.answer,
            "model": self.model,
            "confidence": self.confidence,
            "confidence_label": self.confidence_label,
            "retrieval": self.retrieval.to_dict(),
        }

    def print_text(self, show_context: bool = False) -> None:
        print("\nCâu trả lời:\n")
        print(self.answer.strip())
        print(f"\nĐộ tin cậy: {self.confidence:.0%} ({self.confidence_label})")
        print("\nNguồn truy xuất:")
        seen: set[str] = set()
        for index, chunk in enumerate(self.retrieval.chunks, start=1):
            label = f"S{index}"
            if chunk.citation in seen:
                continue
            seen.add(chunk.citation)
            print(f"- [{label}] {chunk.citation}")
        if show_context:
            print("\nContext đã dùng:")
            for index, chunk in enumerate(self.retrieval.chunks, start=1):
                print(f"\n[S{index}] {chunk.citation}\n{chunk.text_preview}")


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def _query_terms(question: str) -> list[str]:
    normalized = _strip_accents(question.lower())
    normalized = re.sub(r"[^\w\s]", " ", normalized, flags=re.UNICODE)
    terms = [term for term in normalized.split() if len(term) > 1]
    return list(dict.fromkeys(terms))


def _trim_context_text(text: str, question: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text

    normalized_text = _strip_accents(text.lower())
    terms = _query_terms(question)
    candidate_starts = {0}
    for term in terms:
        start = 0
        while True:
            index = normalized_text.find(term, start)
            if index == -1:
                break
            candidate_starts.add(max(0, index - max_chars // 3))
            start = index + len(term)

    best_start = 0
    best_score = -1
    for start in candidate_starts:
        window = normalized_text[start : start + max_chars]
        score = sum(1 for term in terms if term in window)
        if score > best_score:
            best_score = score
            best_start = start

    excerpt = text[best_start : best_start + max_chars].strip()
    if best_start > 0:
        excerpt = "..." + excerpt
    if best_start + max_chars < len(text):
        excerpt = excerpt.rstrip() + "..."
    return excerpt


def _format_context(
    chunks: list[RetrievedChunk],
    question: str = "",
    max_chars_per_chunk: int = DEFAULT_MAX_CONTEXT_CHARS,
) -> str:
    blocks: list[str] = []
    for index, chunk in enumerate(chunks, start=1):
        text = chunk.text.strip()
        text = _trim_context_text(text, question, max_chars_per_chunk)
        blocks.append(
            "\n".join(
                [
                    f"[S{index}]",
                    f"Citation: {chunk.citation}",
                    f"Document: {chunk.document_title or chunk.source_file}",
                    f"Text: {text}",
                ]
            )
        )
    return "\n\n".join(blocks)


def _build_messages(question: str, chunks: list[RetrievedChunk]) -> list[dict[str, str]]:
    context = _format_context(chunks, question=question)
    system_prompt = (
        "Bạn là trợ lý RAG cho sinh viên Học viện Ngân hàng. "
        "Chỉ trả lời dựa trên CONTEXT được cung cấp. "
        "Nếu context không đủ để trả lời, nói rõ là chưa tìm thấy đủ thông tin trong tài liệu. "
        "Trả lời bằng tiếng Việt, ngắn gọn nhưng đủ ý. "
        "Mỗi ý quan trọng phải kèm trích dẫn dạng [S1], [S2]. "
        "Không bịa nguồn, không dùng kiến thức ngoài context."
    )
    user_prompt = f"CONTEXT:\n{context}\n\nQUESTION:\n{question}\n\nHãy trả lời kèm trích dẫn."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def _confidence_label(confidence: float) -> str:
    if confidence >= 0.8:
        return "cao"
    if confidence >= 0.6:
        return "trung bình"
    return "thấp"


def estimate_confidence(retrieval: QueryResult) -> float:
    """Estimate answer confidence from retrieval quality, not from the LLM."""
    chunks = retrieval.chunks
    if not chunks:
        return 0.0

    top = chunks[0]
    top_distance = max(float(top.score), 0.0)
    semantic_strength = 1.0 / (1.0 + top_distance)

    top_source = top.source_path
    source_agreement = sum(1 for chunk in chunks[:3] if chunk.source_path == top_source) / max(min(len(chunks), 3), 1)

    non_empty_context = sum(1 for chunk in chunks if chunk.text.strip()) / len(chunks)
    method_bonus = 0.08 if "keyword" in retrieval.method else 0.0

    confidence = (0.58 * semantic_strength) + (0.24 * source_agreement) + (0.10 * non_empty_context) + method_bonus
    return round(max(0.0, min(confidence, 0.99)), 4)


def answer_question(
    question: str,
    top_k: int = 5,
    model: str | None = None,
    temperature: float = 0.1,
    subject_dir: str | None = None,
    doc_type: str | None = None,
    source_path: str | None = None,
) -> RagAnswer:
    if not config.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is required to generate an answer.")

    retrieval = retrieve_query(
        question=question,
        top_k=top_k,
        subject_dir=subject_dir,
        doc_type=doc_type,
        source_path=source_path,
        use_rerank=True,
        use_hybrid=True,
    )
    if not retrieval.chunks:
        return RagAnswer(
            question=question,
            answer="Chưa tìm thấy tài liệu liên quan trong vector database.",
            model=model or config.LLM_MODEL,
            retrieval=retrieval,
            confidence=0.0,
            confidence_label="thấp",
        )

    llm_model = model or config.LLM_MODEL
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=llm_model,
        messages=_build_messages(question, retrieval.chunks),
        temperature=temperature,
    )
    content = response.choices[0].message.content or ""
    confidence = estimate_confidence(retrieval)
    return RagAnswer(
        question=question,
        answer=content,
        model=llm_model,
        retrieval=retrieval,
        confidence=confidence,
        confidence_label=_confidence_label(confidence),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ask a question with RAG retrieval and OpenAI answer generation.")
    parser.add_argument("question", nargs="*", help="Question to ask. Omit to enter interactive mode.")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--model", default=config.LLM_MODEL)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--subject-dir")
    parser.add_argument("--doc-type")
    parser.add_argument("--source-path")
    parser.add_argument("--json", action="store_true", help="Print full JSON result.")
    parser.add_argument("--show-context", action="store_true", help="Print retrieved context previews.")
    return parser.parse_args()


def _run_single_question(args: argparse.Namespace, question: str) -> None:
    result = answer_question(
        question=question,
        top_k=args.top_k,
        model=args.model,
        temperature=args.temperature,
        subject_dir=args.subject_dir,
        doc_type=args.doc_type,
        source_path=args.source_path,
    )
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        result.print_text(show_context=args.show_context)


def main() -> None:
    args = parse_args()
    if args.question:
        _run_single_question(args, " ".join(args.question).strip())
        return

    print("RAG CLI. Nhập câu hỏi, hoặc gõ 'exit' để thoát.")
    while True:
        try:
            question = input("\nBạn: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question.lower() in {"exit", "quit", "q"}:
            break
        try:
            _run_single_question(args, question)
        except Exception as exc:
            print(f"Lỗi: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    main()
