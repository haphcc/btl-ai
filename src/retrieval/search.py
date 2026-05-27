from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.core.config import config
from src.ingestion.vector_store import DEFAULT_CHUNKS_PATH, get_embedding_function, load_chunks


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOP_K = 6
DEFAULT_FETCH_MULTIPLIER = 3


@dataclass(frozen=True)
class EmbeddingConfig:
    provider: str
    model: str
    collection_name: str
    db_path: str


@dataclass
class RetrievedChunk:
    rank: int
    chunk_id: str
    text: str
    score: float
    source_path: str
    source_file: str
    subject_dir: str
    subject_name: str
    document_title: str
    doc_type: str
    section_path: list[str]
    chunk_index: int
    token_estimate: int

    @property
    def citation(self) -> str:
        section = " > ".join(self.section_path) if self.section_path else "unknown section"
        return f"{self.source_path} | {section}"

    @property
    def text_preview(self) -> str:
        return self.text[:300] + ("..." if len(self.text) > 300 else "")

    def to_dict(self) -> dict[str, Any]:
        return {
            "rank": self.rank,
            "chunk_id": self.chunk_id,
            "score": round(float(self.score), 4),
            "text": self.text,
            "text_preview": self.text_preview,
            "citation": self.citation,
            "source_path": self.source_path,
            "source_file": self.source_file,
            "subject_dir": self.subject_dir,
            "subject_name": self.subject_name,
            "document_title": self.document_title,
            "doc_type": self.doc_type,
            "section_path": self.section_path,
            "chunk_index": self.chunk_index,
            "token_estimate": self.token_estimate,
        }


@dataclass
class QueryResult:
    query: str
    top_k: int
    method: str
    embedding: EmbeddingConfig
    chunks: list[RetrievedChunk] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "top_k": self.top_k,
            "method": self.method,
            "embedding": self.embedding.__dict__,
            "chunks": [chunk.to_dict() for chunk in self.chunks],
        }

    def print_summary(self) -> None:
        print(json.dumps(self.to_dict(), ensure_ascii=False, indent=2))


def embedding_config(
    db_path: Path | str | None = None,
    collection_name: str | None = None,
    embedding_provider: str | None = None,
) -> EmbeddingConfig:
    provider = (embedding_provider or config.EMBEDDING_PROVIDER).lower()
    return EmbeddingConfig(
        provider=provider,
        model=config.EMBEDDING_MODEL if provider == "openai" else "hash-384",
        collection_name=collection_name or config.CHROMA_COLLECTION_NAME,
        db_path=str(db_path or config.VECTOR_DB_PATH),
    )


def _open_collection(
    db_path: Path | str | None = None,
    collection_name: str | None = None,
    embedding_provider: str | None = None,
):
    import chromadb

    settings = embedding_config(db_path, collection_name, embedding_provider)
    resolved_db_path = Path(settings.db_path)
    if not resolved_db_path.exists():
        raise FileNotFoundError(
            f"ChromaDB path does not exist: {resolved_db_path}. "
            "Build it first with: python -m src.ingestion.vector_store rebuild"
        )

    client = chromadb.PersistentClient(path=str(resolved_db_path))
    return client.get_collection(
        name=settings.collection_name,
        embedding_function=get_embedding_function(settings.provider),
    )


def _parse_section_path(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return [value] if value else []
        if isinstance(parsed, list):
            return [str(item) for item in parsed]
        return [str(parsed)]
    return []


def _build_where_filter(
    subject_dir: str | list[str] | None = None,
    doc_type: str | list[str] | None = None,
    source_path: str | None = None,
) -> dict[str, Any] | None:
    conditions: list[dict[str, Any]] = []

    if subject_dir:
        if isinstance(subject_dir, str):
            conditions.append({"subject_dir": {"$eq": subject_dir}})
        else:
            conditions.append({"subject_dir": {"$in": subject_dir}})

    if doc_type:
        if isinstance(doc_type, str):
            conditions.append({"doc_type": {"$eq": doc_type}})
        else:
            conditions.append({"doc_type": {"$in": doc_type}})

    if source_path:
        conditions.append({"source_path": {"$eq": source_path}})

    if not conditions:
        return None
    if len(conditions) == 1:
        return conditions[0]
    return {"$and": conditions}


def _metadata_matches(
    metadata: dict[str, Any],
    subject_dir: str | list[str] | None = None,
    doc_type: str | list[str] | None = None,
    source_path: str | None = None,
) -> bool:
    if subject_dir:
        allowed = {subject_dir} if isinstance(subject_dir, str) else set(subject_dir)
        if metadata.get("subject_dir") not in allowed:
            return False
    if doc_type:
        allowed = {doc_type} if isinstance(doc_type, str) else set(doc_type)
        if metadata.get("doc_type") not in allowed:
            return False
    if source_path and metadata.get("source_path") != source_path:
        return False
    return True


def _chunk_from_record(
    rank: int,
    chunk_id: str,
    text: str,
    metadata: dict[str, Any],
    score: float,
) -> RetrievedChunk:
    section_path = _parse_section_path(metadata.get("section_path", "[]"))
    if not section_path:
        section_path = [
            str(
                metadata.get("chapter_title")
                or metadata.get("document_title")
                or metadata.get("source_file")
                or "unknown section"
            )
        ]

    return RetrievedChunk(
        rank=rank,
        chunk_id=chunk_id,
        text=text,
        score=float(score),
        source_path=str(metadata.get("source_path", "")),
        source_file=str(metadata.get("source_file", "")),
        subject_dir=str(metadata.get("subject_dir", "")),
        subject_name=str(metadata.get("subject_name", "")),
        document_title=str(metadata.get("document_title", "")),
        doc_type=str(metadata.get("doc_type", "")),
        section_path=section_path,
        chunk_index=int(metadata.get("chunk_index") or 0),
        token_estimate=int(metadata.get("token_estimate") or 0),
    )


def retrieve(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    subject_dir: str | list[str] | None = None,
    doc_type: str | list[str] | None = None,
    source_path: str | None = None,
    db_path: Path | str | None = None,
    collection_name: str | None = None,
    embedding_provider: str | None = None,
) -> list[RetrievedChunk]:
    if not query.strip():
        raise ValueError("query must not be empty")
    if top_k < 1:
        raise ValueError("top_k must be >= 1")

    collection = _open_collection(db_path, collection_name, embedding_provider)
    where = _build_where_filter(subject_dir, doc_type, source_path)

    params: dict[str, Any] = {
        "query_texts": [query],
        "n_results": top_k,
        "include": ["documents", "metadatas", "distances"],
    }
    if where:
        params["where"] = where

    raw = collection.query(**params)
    ids = raw.get("ids", [[]])[0]
    documents = raw.get("documents", [[]])[0]
    metadatas = raw.get("metadatas", [[]])[0]
    distances = raw.get("distances", [[]])[0]

    return [
        _chunk_from_record(rank, chunk_id, document, metadata or {}, distance)
        for rank, (chunk_id, document, metadata, distance) in enumerate(
            zip(ids, documents, metadatas, distances),
            start=1,
        )
    ]


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def _tokenize(text: str) -> list[str]:
    normalized = _strip_accents(text.lower())
    normalized = re.sub(r"[^\w\s]", " ", normalized, flags=re.UNICODE)
    return [token for token in normalized.split() if len(token) > 1]


def _bm25_score(query_tokens: list[str], document: str, avg_dl: float = 300.0) -> float:
    tokens = _tokenize(document)
    if not tokens:
        return 0.0

    k1 = 1.5
    b = 0.75
    dl = len(tokens)
    term_frequency: dict[str, int] = {}
    for token in tokens:
        term_frequency[token] = term_frequency.get(token, 0) + 1

    score = 0.0
    for token in query_tokens:
        tf = term_frequency.get(token, 0)
        if tf == 0:
            continue
        idf = math.log(2.0)
        denominator = tf + k1 * (1 - b + b * dl / max(avg_dl, 1.0))
        score += idf * ((tf * (k1 + 1)) / denominator)
    return score


def rerank(chunks: list[RetrievedChunk], query: str) -> list[RetrievedChunk]:
    if not chunks:
        return []

    query_tokens = _tokenize(query)
    avg_dl = sum(max(chunk.token_estimate, 1) for chunk in chunks) / len(chunks)

    scored: list[tuple[float, RetrievedChunk]] = []
    for chunk in chunks:
        lexical_score = _bm25_score(query_tokens, chunk.text, avg_dl)
        semantic_score = 1.0 / (1.0 + max(chunk.score, 0.0))
        lexical_norm = lexical_score / (lexical_score + 1.0) if lexical_score else 0.0
        scored.append((0.65 * semantic_score + 0.35 * lexical_norm, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    reranked: list[RetrievedChunk] = []
    for rank, (_, chunk) in enumerate(scored, start=1):
        chunk.rank = rank
        reranked.append(chunk)
    return reranked


def keyword_fallback(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    subject_dir: str | list[str] | None = None,
    doc_type: str | list[str] | None = None,
    source_path: str | None = None,
    chunks_path: Path | str = DEFAULT_CHUNKS_PATH,
) -> list[RetrievedChunk]:
    query_tokens = _tokenize(query)
    if not query_tokens:
        return []

    query_token_set = set(query_tokens)
    scored: list[tuple[float, dict[str, Any]]] = []
    for chunk in load_chunks(Path(chunks_path)):
        if not _metadata_matches(chunk, subject_dir, doc_type, source_path):
            continue

        document_tokens = _tokenize(chunk.get("text", ""))
        if not document_tokens:
            continue

        overlap = len(query_token_set & set(document_tokens)) / len(query_token_set)
        bm25 = _bm25_score(query_tokens, chunk.get("text", ""))
        phrase_bonus = 1.0 if _strip_accents(query.lower()) in _strip_accents(chunk.get("text", "").lower()) else 0.0
        score = overlap + bm25 + phrase_bonus
        if score > 0:
            scored.append((score, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    results: list[RetrievedChunk] = []
    for rank, (score, chunk) in enumerate(scored[:top_k], start=1):
        results.append(
            _chunk_from_record(
                rank=rank,
                chunk_id=str(chunk.get("chunk_id", "")),
                text=str(chunk.get("text", "")),
                metadata=chunk,
                score=1.0 / (1.0 + score),
            )
        )
    return results


def _merge_semantic_and_keyword(
    semantic_chunks: list[RetrievedChunk],
    keyword_chunks: list[RetrievedChunk],
    top_k: int,
) -> list[RetrievedChunk]:
    merged: dict[str, tuple[float, RetrievedChunk]] = {}

    for index, chunk in enumerate(semantic_chunks):
        merged[chunk.chunk_id] = (merged.get(chunk.chunk_id, (0.0, chunk))[0] + 1.0 / (index + 1), chunk)

    for index, chunk in enumerate(keyword_chunks):
        existing_score, existing_chunk = merged.get(chunk.chunk_id, (0.0, chunk))
        merged[chunk.chunk_id] = (existing_score + 1.25 / (index + 1), existing_chunk)

    ordered = sorted(merged.values(), key=lambda item: item[0], reverse=True)
    chunks: list[RetrievedChunk] = []
    for rank, (_, chunk) in enumerate(ordered[:top_k], start=1):
        chunk.rank = rank
        chunks.append(chunk)
    return chunks


def query(
    question: str,
    top_k: int = DEFAULT_TOP_K,
    subject_dir: str | list[str] | None = None,
    doc_type: str | list[str] | None = None,
    source_path: str | None = None,
    use_rerank: bool = True,
    use_hybrid: bool = True,
    fallback_threshold: float = 1.5,
    db_path: Path | str | None = None,
    collection_name: str | None = None,
    embedding_provider: str | None = None,
) -> QueryResult:
    settings = embedding_config(db_path, collection_name, embedding_provider)
    fetch_k = max(top_k * DEFAULT_FETCH_MULTIPLIER, top_k)
    method = "semantic"

    chunks = retrieve(
        query=question,
        top_k=fetch_k if use_rerank or use_hybrid else top_k,
        subject_dir=subject_dir,
        doc_type=doc_type,
        source_path=source_path,
        db_path=settings.db_path,
        collection_name=settings.collection_name,
        embedding_provider=settings.provider,
    )

    if use_rerank:
        chunks = rerank(chunks, question)
        method = "semantic+rerank"

    chunks = chunks[:top_k]

    if use_hybrid:
        keyword_chunks = keyword_fallback(
            question,
            top_k=top_k,
            subject_dir=subject_dir,
            doc_type=doc_type,
            source_path=source_path,
        )
        if keyword_chunks:
            chunks = _merge_semantic_and_keyword(chunks, keyword_chunks, top_k)
            method = f"{method}+keyword"

    if not chunks or chunks[0].score > fallback_threshold:
        fallback_chunks = keyword_fallback(
            question,
            top_k=top_k,
            subject_dir=subject_dir,
            doc_type=doc_type,
            source_path=source_path,
        )
        if fallback_chunks:
            chunks = fallback_chunks
            method = "keyword_fallback"

    return QueryResult(
        query=question,
        top_k=top_k,
        method=method,
        embedding=settings,
        chunks=chunks,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Retrieve top-k chunks from ChromaDB.")
    parser.add_argument("question")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--subject-dir")
    parser.add_argument("--doc-type")
    parser.add_argument("--source-path")
    parser.add_argument("--db-path", type=Path)
    parser.add_argument("--collection", default=config.CHROMA_COLLECTION_NAME)
    parser.add_argument("--embedding-provider", choices=["openai", "hash"], default=config.EMBEDDING_PROVIDER)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--no-hybrid", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = query(
        question=args.question,
        top_k=args.top_k,
        subject_dir=args.subject_dir,
        doc_type=args.doc_type,
        source_path=args.source_path,
        use_rerank=not args.no_rerank,
        use_hybrid=not args.no_hybrid,
        db_path=args.db_path,
        collection_name=args.collection,
        embedding_provider=args.embedding_provider,
    )
    result.print_summary()


if __name__ == "__main__":
    main()
