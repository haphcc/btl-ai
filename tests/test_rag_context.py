import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.generation.rag_answer import _format_context
from src.retrieval.search import keyword_fallback


def test_context_excerpt_keeps_nckh_score_table_answer():
    question = "Giải nhất, nhì, ba cấp bộ GD&ĐT NCKH được cộng mấy điểm"
    chunks = keyword_fallback(question, top_k=1)

    context = _format_context(chunks, question=question, max_chars_per_chunk=1400)

    assert "Cấp Bộ GD&ĐT" in context
    assert "Nhất, nhì, ba" in context
    assert "10.0 điểm" in context
    assert "khóa luận tốt nghiệp" in context
