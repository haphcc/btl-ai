from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.core.config import config


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHUNKS_PATH = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"
DEFAULT_COLLECTION_NAME = config.CHROMA_COLLECTION_NAME

REQUIRED_FIELDS = {
    "chunk_id",
    "text",
    "source_path",
    "source_file",
    "subject_dir",
    "subject_name",
    "document_title",
    "doc_type",
    "section_path",
    "chunk_index",
    "char_start",
    "char_end",
    "token_estimate",
    "content_hash",
    "source_hash",
    "created_at",
}


class ChunkValidationError(ValueError):
    pass


class HashEmbeddingFunction:
    """Small deterministic embedding function for offline tests and local smoke checks."""

    def __init__(self, dimensions: int = 384):
        self.dimensions = dimensions

    def name(self) -> str:
        return f"hash-{self.dimensions}"

    def __call__(self, input: list[str]) -> list[list[float]]:
        return [self._embed(text) for text in input]

    def embed_query(self, input: list[str]) -> list[list[float]]:
        return self(input)

    def embed_documents(self, input: list[str]) -> list[list[float]]:
        return self(input)

    def _embed(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        words = text.lower().split()
        for word in words:
            digest = hashlib.sha256(word.encode("utf-8")).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimensions
            sign = 1.0 if digest[4] % 2 == 0 else -1.0
            vector[index] += sign
        norm = sum(value * value for value in vector) ** 0.5 or 1.0
        return [value / norm for value in vector]


def load_chunks(path: Path = DEFAULT_CHUNKS_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Chunk file not found: {path}")

    chunks: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ChunkValidationError(f"Invalid JSON at line {line_no}: {exc}") from exc
            item["_line_no"] = line_no
            chunks.append(item)
    return chunks


def validate_chunks(chunks: list[dict[str, Any]], project_root: Path = PROJECT_ROOT) -> dict[str, Any]:
    errors: list[str] = []
    chunk_ids: list[str] = []
    source_paths: set[str] = set()

    for index, chunk in enumerate(chunks):
        label = f"line {chunk.get('_line_no', index + 1)}"
        missing = sorted(REQUIRED_FIELDS - set(chunk))
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(missing)}")

        chunk_id = chunk.get("chunk_id")
        if not isinstance(chunk_id, str) or not chunk_id.strip():
            errors.append(f"{label}: chunk_id is empty or not a string")
        else:
            chunk_ids.append(chunk_id)

        text = chunk.get("text")
        if not isinstance(text, str) or not text.strip():
            errors.append(f"{label}: text is empty or not a string")

        source_path = chunk.get("source_path")
        if not isinstance(source_path, str) or not source_path.strip():
            errors.append(f"{label}: source_path is empty or not a string")
        else:
            source_paths.add(source_path)
            if not (project_root / source_path).exists():
                errors.append(f"{label}: source_path does not exist: {source_path}")

        section_path = chunk.get("section_path")
        if not isinstance(section_path, list) or not all(isinstance(item, str) for item in section_path):
            errors.append(f"{label}: section_path must be a list of strings")

        token_estimate = chunk.get("token_estimate")
        if not isinstance(token_estimate, int):
            errors.append(f"{label}: token_estimate must be an integer")
        elif token_estimate <= 0:
            errors.append(f"{label}: token_estimate must be positive")
        elif token_estimate > config.CHUNK_HARD_MAX:
            errors.append(f"{label}: token_estimate exceeds expected hard max: {token_estimate}")

        chunk_index = chunk.get("chunk_index")
        if not isinstance(chunk_index, int) or chunk_index < 0:
            errors.append(f"{label}: chunk_index must be a non-negative integer")

    duplicates = [chunk_id for chunk_id, count in Counter(chunk_ids).items() if count > 1]
    for chunk_id in duplicates:
        errors.append(f"duplicate chunk_id: {chunk_id}")

    processed_files = {path.relative_to(project_root).as_posix() for path in (project_root / "data" / "processed").rglob("*.md")}
    files_without_chunks = sorted(processed_files - source_paths)
    for source_path in files_without_chunks:
        errors.append(f"source file has no chunk: {source_path}")

    return {
        "chunk_count": len(chunks),
        "unique_ids": len(set(chunk_ids)),
        "source_file_count": len(source_paths),
        "files_without_chunks": files_without_chunks,
        "errors": errors,
    }


def chroma_metadata(chunk: dict[str, Any]) -> dict[str, str | int | float | bool | None]:
    section_path = chunk.get("section_path") or []
    metadata = {
        "source_path": chunk.get("source_path"),
        "source_file": chunk.get("source_file"),
        "subject_dir": chunk.get("subject_dir"),
        "subject_name": chunk.get("subject_name"),
        "document_title": chunk.get("document_title"),
        "doc_type": chunk.get("doc_type"),
        "chapter_no": chunk.get("chapter_no"),
        "chapter_title": chunk.get("chapter_title"),
        "section_path": json.dumps(section_path, ensure_ascii=False),
        "section_path_text": " > ".join(section_path),
        "chunk_index": chunk.get("chunk_index"),
        "char_start": chunk.get("char_start"),
        "char_end": chunk.get("char_end"),
        "token_estimate": chunk.get("token_estimate"),
        "content_hash": chunk.get("content_hash"),
        "source_hash": chunk.get("source_hash"),
        "created_at": chunk.get("created_at"),
    }
    return {key: value for key, value in metadata.items() if value is not None}


def chunks_to_chroma_records(chunks: list[dict[str, Any]]) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    ids = [chunk["chunk_id"] for chunk in chunks]
    documents = [chunk["text"] for chunk in chunks]
    metadatas = [chroma_metadata(chunk) for chunk in chunks]
    return ids, documents, metadatas


def batched(items: list[Any], batch_size: int) -> Iterable[list[Any]]:
    for start in range(0, len(items), batch_size):
        yield items[start : start + batch_size]


def get_embedding_function(provider: str | None = None):
    provider = (provider or config.EMBEDDING_PROVIDER).lower()
    if provider == "hash":
        dimensions = int(os.getenv("HASH_EMBEDDING_DIMENSIONS", "384"))
        return HashEmbeddingFunction(dimensions=dimensions)
    if provider == "openai":
        from chromadb.utils import embedding_functions

        if not config.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY is required when EMBEDDING_PROVIDER=openai")
        return embedding_functions.OpenAIEmbeddingFunction(
            api_key=config.OPENAI_API_KEY,
            model_name=config.EMBEDDING_MODEL,
        )
    raise ValueError(f"Unsupported embedding provider: {provider}")


def rebuild_chroma_index(
    chunks_path: Path = DEFAULT_CHUNKS_PATH,
    db_path: Path | str = config.VECTOR_DB_PATH,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    embedding_provider: str | None = None,
    batch_size: int = 64,
    reset_collection: bool = True,
) -> dict[str, Any]:
    import chromadb

    chunks = load_chunks(chunks_path)
    validation = validate_chunks(chunks)
    if validation["errors"]:
        raise ChunkValidationError("\n".join(validation["errors"]))

    client = chromadb.PersistentClient(path=str(db_path))
    if reset_collection:
        try:
            client.delete_collection(collection_name)
        except Exception:
            pass

    embedding_function = get_embedding_function(embedding_provider)
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
        metadata={"source": str(chunks_path), "embedding_model": config.EMBEDDING_MODEL},
    )

    ids, documents, metadatas = chunks_to_chroma_records(chunks)
    inserted = 0
    for id_batch, doc_batch, metadata_batch in zip(
        batched(ids, batch_size),
        batched(documents, batch_size),
        batched(metadatas, batch_size),
    ):
        collection.upsert(ids=id_batch, documents=doc_batch, metadatas=metadata_batch)
        inserted += len(id_batch)

    return {
        "collection": collection_name,
        "db_path": str(db_path),
        "embedding_provider": embedding_provider or config.EMBEDDING_PROVIDER,
        "chunk_count": len(chunks),
        "inserted": inserted,
        "collection_count": collection.count(),
    }


def collection_count(
    db_path: Path | str = config.VECTOR_DB_PATH,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    embedding_provider: str | None = None,
) -> dict[str, Any]:
    import chromadb

    client = chromadb.PersistentClient(path=str(db_path))
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=get_embedding_function(embedding_provider),
    )
    return {"collection": collection_name, "db_path": str(db_path), "collection_count": collection.count()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate chunks and rebuild the Chroma vector index.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate chunks.jsonl before embedding.")
    validate_parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNKS_PATH)

    rebuild_parser = subparsers.add_parser("rebuild", help="Rebuild the Chroma collection from chunks.jsonl.")
    rebuild_parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNKS_PATH)
    rebuild_parser.add_argument("--db-path", type=Path, default=Path(config.VECTOR_DB_PATH))
    rebuild_parser.add_argument("--collection", default=DEFAULT_COLLECTION_NAME)
    rebuild_parser.add_argument("--embedding-provider", choices=["openai", "hash"], default=config.EMBEDDING_PROVIDER)
    rebuild_parser.add_argument("--batch-size", type=int, default=64)
    rebuild_parser.add_argument("--append", action="store_true", help="Upsert without deleting the collection first.")

    count_parser = subparsers.add_parser("count", help="Show Chroma collection count.")
    count_parser.add_argument("--db-path", type=Path, default=Path(config.VECTOR_DB_PATH))
    count_parser.add_argument("--collection", default=DEFAULT_COLLECTION_NAME)
    count_parser.add_argument("--embedding-provider", choices=["openai", "hash"], default=config.EMBEDDING_PROVIDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "validate":
        report = validate_chunks(load_chunks(args.chunks))
    elif args.command == "rebuild":
        report = rebuild_chroma_index(
            chunks_path=args.chunks,
            db_path=args.db_path,
            collection_name=args.collection,
            embedding_provider=args.embedding_provider,
            batch_size=args.batch_size,
            reset_collection=not args.append,
        )
    elif args.command == "count":
        report = collection_count(
            db_path=args.db_path,
            collection_name=args.collection,
            embedding_provider=args.embedding_provider,
        )
    else:
        raise ValueError(f"Unknown command: {args.command}")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
