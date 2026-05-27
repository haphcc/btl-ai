import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.ingestion.vector_store import rebuild_chroma_index
from src.retrieval.search import keyword_fallback, query, retrieve


CHUNKS_PATH = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"
COLLECTION_NAME = "test_retrieval_chunks"

SMOKE_CASES = [
    (
        "chuyển đổi tín chỉ",
        [
            "data/processed/QuyDinhQuyCheHVNH/QD 2786 - Quy dinh cong nhan ket qua hoc tap va chuyen doi tin chi.md",
            "data/processed/QuyDinhQuyCheHVNH/QD 2862 - Huong dan quy doi tin chi HVNH va ECTS.md",
            "data/processed/QuyDinhQuyCheHVNH/QD 309 - Cong nhan chung chi nghe nghiep du dieu kien chuyen doi tin chi.md",
            "data/processed/QuyDinhQuyCheHVNH/NQ 269 - Quy che dao tao dai hoc chinh quy cua HVNH.md",
        ],
    ),
    (
        "chuẩn đầu ra ngoại ngữ",
        [
            "data/processed/QuyDinhQuyCheHVNH/QD 3337 - Quy dinh chuan dau ra ngoai ngu va CNTT.md",
        ],
    ),
    (
        "điểm khuyến khích nghiên cứu khoa học",
        [
            "data/processed/QuyDinhQuyCheHVNH/QD 422 - Cong diem khuyen khich sinh vien NCKH dat giai.md",
            "data/processed/QuyDinhQuyCheHVNH/NQ 269 - Quy che dao tao dai hoc chinh quy cua HVNH.md",
        ],
    ),
    (
        "T-SQL trigger",
        [
            "data/processed/csdl/Chuong 5 - Ngon ngu T-SQL.md",
        ],
    ),
    (
        "phụ thuộc hàm",
        [
            "data/processed/tkcsdl/Chuong 2 - Cac khai niem trong thiet ke co so du lieu quan he.md",
            "data/processed/tkcsdl/Chuong 4 - Thiet ke CSDL muc logic.md",
        ],
    ),
    (
        "kiểm định giả thuyết",
        [
            "data/processed/xstk/bai_08_kiem_dinh_gia_thuyet_thong_ke.md",
        ],
    ),
    (
        "lan truyền ngược",
        [
            "data/processed/tri tue nhan tao/Lecture 8-9 - Neural networks.md",
        ],
    ),
    (
        "học phần tiên quyết",
        [
            "data/processed/QuyDinhQuyCheHVNH/NQ 269 - Quy che dao tao dai hoc chinh quy cua HVNH.md",
        ],
    ),
]


@pytest.fixture(scope="session")
def retrieval_db(tmp_path_factory):
    pytest.importorskip("chromadb")
    db_path = tmp_path_factory.mktemp("retrieval_chroma")
    rebuild_chroma_index(
        chunks_path=CHUNKS_PATH,
        db_path=db_path,
        collection_name=COLLECTION_NAME,
        embedding_provider="hash",
        batch_size=128,
    )
    return db_path


def test_retrieve_returns_chroma_chunks_with_citations(retrieval_db):
    chunks = retrieve(
        "T-SQL trigger",
        top_k=5,
        db_path=retrieval_db,
        collection_name=COLLECTION_NAME,
        embedding_provider="hash",
    )

    assert chunks
    assert len(chunks) <= 5
    for chunk in chunks:
        assert chunk.text.strip()
        assert chunk.source_path
        assert chunk.section_path
        assert chunk.citation


@pytest.mark.parametrize(("question", "expected_paths"), SMOKE_CASES)
def test_query_smoke_top_k_has_relevant_citation(retrieval_db, question, expected_paths):
    result = query(
        question,
        top_k=6,
        db_path=retrieval_db,
        collection_name=COLLECTION_NAME,
        embedding_provider="hash",
        use_rerank=True,
        use_hybrid=True,
    )

    top_paths = [chunk.source_path for chunk in result.chunks[:3]]
    assert result.chunks, question
    assert result.chunks[0].source_path in expected_paths
    assert any(path in expected_paths for path in top_paths)
    for chunk in result.chunks:
        assert chunk.source_path
        assert chunk.section_path


@pytest.mark.parametrize(("question", "expected_paths"), SMOKE_CASES)
def test_keyword_fallback_smoke_top_1_is_expected_file(question, expected_paths):
    chunks = keyword_fallback(question, top_k=3)

    assert chunks, question
    assert chunks[0].source_path in expected_paths
    assert chunks[0].section_path
