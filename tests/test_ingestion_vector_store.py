import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.ingestion.vector_store import (
    chunks_to_chroma_records,
    load_chunks,
    rebuild_chroma_index,
    validate_chunks,
)


CHUNKS_PATH = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"


def test_chunks_jsonl_is_valid_for_embedding():
    chunks = load_chunks(CHUNKS_PATH)
    report = validate_chunks(chunks)

    assert report["chunk_count"] > 0
    assert report["chunk_count"] == report["unique_ids"]
    assert report["errors"] == []
    assert report["files_without_chunks"] == []


def test_chroma_record_shape_uses_scalar_metadata():
    chunks = load_chunks(CHUNKS_PATH)[:3]
    ids, documents, metadatas = chunks_to_chroma_records(chunks)

    assert len(ids) == len(documents) == len(metadatas) == 3
    assert all(ids)
    assert all(document.strip() for document in documents)
    for metadata in metadatas:
        assert "source_path" in metadata
        assert "document_title" in metadata
        assert "section_path" in metadata
        assert isinstance(metadata["section_path"], str)
        json.loads(metadata["section_path"])


def test_rebuild_chroma_index_offline_hash_embedding(tmp_path):
    chromadb = pytest.importorskip("chromadb")
    del chromadb

    report = rebuild_chroma_index(
        chunks_path=CHUNKS_PATH,
        db_path=tmp_path / "chroma",
        collection_name="test_chunks",
        embedding_provider="hash",
        batch_size=128,
    )

    assert report["inserted"] == report["chunk_count"]
    assert report["collection_count"] == report["chunk_count"]
