import sys
from pathlib import Path
import json
import uuid
import re
import time

# Add project root to path to ensure clean relative imports
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from src.core.config import config
from src.generation.rag_answer import answer_question, estimate_confidence

# Define chat history save directory
CHAT_HISTORY_DIR = PROJECT_ROOT / "data" / "chat_history"
CHAT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)

# Friendly Vietnamese subject mapping based on folder names in data/processed/
SUBJECT_MAP = {
    "ATBMTT": "An toàn & Bảo mật Thông tin",
    "QuyDinhQuyCheHVNH": "Quy chế & Quy định Học viện Ngân hàng",
    "c++ nâng cao": "Lập trình C++ Nâng cao",
    "csdl": "Cơ sở Dữ liệu",
    "cslt": "Cơ sở Lập trình",
    "ctdlgt": "Cấu trúc Dữ liệu & Giải thuật",
    "hqtcsdl": "Hệ Quản trị Cơ sở Dữ liệu",
    "htttql": "Hệ thống Thông tin Quản lý (MIS)",
    "java": "Lập trình Hướng đối tượng với Java",
    "khaiphavphantichdulieu": "Khai phá & Phân tích Dữ liệu",
    "kientrucphanmem": "Kiến trúc Phần mềm",
    "ktmthdh": "Kiến trúc Máy tính & Hệ điều hành",
    "laptrinh dotnet": "Lập trình .NET (C#)",
    "laptrinhnangcaoC": "Lập trình C Nâng cao",
    "mang": "Mạng Máy tính",
    "nhập môn cntt": "Nhập môn Công nghệ Thông tin",
    "nlsud": "Năng lực Số ứng dụng",
    "php": "Lập trình Web với PHP",
    "pttkht": "Phân tích & Thiết kế Hệ thống",
    "thietkeweb": "Thiết kế Web (HTML/CSS/JS)",
    "tkcsdl": "Thiết kế Cơ sở Dữ liệu",
    "tri tue nhan tao": "Trí tuệ Nhân tạo (AI)",
    "trr": "Toán Rời rạc",
    "xstk": "Xác suất Thống kê"
}

# --- HELPER FUNCTIONS ---
def get_client_id():
    """Gets or generates a persistent client ID via URL query parameters to emulate browser local storage."""
    if "client_id" not in st.query_params:
        new_id = str(uuid.uuid4())
        st.query_params["client_id"] = new_id
        return new_id
    return st.query_params["client_id"]

def load_persisted_history(client_id: str) -> list:
    """Loads chat history for a specific client ID from server storage."""
    file_path = CHAT_HISTORY_DIR / f"{client_id}.json"
    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_persisted_history(client_id: str, messages: list):
    """Saves chat history for a specific client ID to server storage."""
    file_path = CHAT_HISTORY_DIR / f"{client_id}.json"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except Exception as e:
        st.error(f"Lỗi lưu trữ lịch sử: {e}")

def list_available_sessions():
    """Scans CHAT_HISTORY_DIR and returns a sorted list of session details."""
    sessions = []
    for file_path in CHAT_HISTORY_DIR.glob("*.json"):
        session_id = file_path.stem
        try:
            mtime = file_path.stat().st_mtime
            import datetime
            dt = datetime.datetime.fromtimestamp(mtime)
            formatted_time = dt.strftime("%H:%M - %d/%m")
            
            with open(file_path, "r", encoding="utf-8") as f:
                msgs = json.load(f)
                
            if msgs:
                first_user = next((m["content"] for m in msgs if m["role"] == "user"), None)
                if first_user:
                    title = first_user[:30] + ("..." if len(first_user) > 30 else "")
                else:
                    title = "Cuộc trò chuyện mới"
            else:
                title = "Cuộc trò chuyện trống"
                
            sessions.append({
                "id": session_id,
                "title": f"💬 {title} ({formatted_time})",
                "time": mtime
            })
        except Exception:
            continue
            
    sessions.sort(key=lambda s: s["time"], reverse=True)
    return sessions

def extract_concise_snippet(text: str, query: str, max_words: int = 35) -> str:
    """Extracts an ultra-concise context snippet centered around the query terms."""
    cleaned = " ".join(text.split())
    words = cleaned.split()
    
    if len(words) <= max_words:
        return cleaned
        
    query_words = [w.lower() for w in query.split() if len(w) > 2]
    if not query_words:
        return " ".join(words[:max_words]) + "..."
        
    best_start = 0
    best_score = -1
    
    for i in range(len(words) - max_words + 1):
        window = " ".join(words[i:i+max_words]).lower()
        score = sum(3 if w in window else 0 for w in query_words)
        if score > best_score:
            best_score = score
            best_start = i
            
    snippet_words = words[best_start:best_start+max_words]
    snippet = " ".join(snippet_words)
    
    if best_start > 0:
        snippet = "..." + snippet
    if best_start + max_words < len(words):
        snippet = snippet + "..."
    return snippet

def format_latex(text: str) -> str:
    """Converts LaTeX delimiters commonly used by LLMs (\\(...\\) and \\[...\\]) to Streamlit-compatible delimiters ($...$ and $$...$$)."""
    if not text:
        return ""
    text = text.replace("\\[", "$$").replace("\\]", "$$")
    text = text.replace("\\(", "$").replace("\\)", "$")
    return text

def render_citations(citations: list[dict], query: str) -> None:
    """Renders a highly compact, gorgeous, and concise citation view using tabs."""
    if not citations:
        return
        
    with st.expander("🔍 Xem nguồn trích dẫn học tập (Rất ngắn gọn)"):
        tab1, tab2 = st.tabs(["📋 Danh sách tài liệu", "📝 Đoạn trích tiêu biểu"])
        
        with tab1:
            markdown_lines = [
                "| Mã | Tên tài liệu / Văn bản | Chương / Mục | Khớp Ngữ Nghĩa * |",
                "| :--- | :--- | :--- | :---: |"
            ]
            for cite in citations:
                title = cite["title"].replace(".md", "")
                markdown_lines.append(
                    f"| `[S{cite['rank']}]` | **{title}** | *{cite['section']}* | `{cite['score']:.0%}` |"
                )
            st.markdown("\n".join(markdown_lines))
            st.caption(r"* *Ghi chú: Tài liệu được sắp xếp và lựa chọn tối ưu theo phương pháp Tìm kiếm Lai (Hybrid Search: Ngữ nghĩa + Từ khóa BM25 & Rerank) để đảm bảo độ chính xác thực tế cao nhất, không chỉ dựa trên độ khớp ngữ nghĩa đơn thuần.*")
            
        with tab2:
            for cite in citations:
                title = cite["title"].replace(".md", "")
                snippet = extract_concise_snippet(cite["full_text"], query)
                st.markdown(f"""
                <div class="citation-box" style="margin-bottom: 0.5rem; padding: 0.5rem 0.8rem;">
                    <div class="citation-header" style="margin-bottom: 0.2rem;">
                        <span style="font-size: 0.85rem;">`[S{cite['rank']}]` {title} &mdash; <small style="color: #64748B;">{cite['section']}</small></span>
                    </div>
                    <div class="citation-excerpt" style="font-size: 0.85rem;">"{snippet}"</div>
                </div>
                """, unsafe_allow_html=True)

def citation_validity(answer: str, citations: list[dict]) -> float:
    """Return the share of [Sx] citations that point to retrieved sources."""
    cited_numbers = [int(match) for match in re.findall(r"\[S(\d+)\]", answer or "")]
    if not cited_numbers:
        return 0.0
    valid_ranks = {int(cite["rank"]) for cite in citations}
    valid_count = sum(1 for number in cited_numbers if number in valid_ranks)
    return valid_count / len(cited_numbers)

def source_relevance(citations: list[dict]) -> float:
    """Estimate source relevance from retrieved chunk scores for this question."""
    scores = [float(cite.get("score", 0.0)) for cite in citations]
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def render_rag_metrics(meta: dict, badges_html: str = "") -> None:
    """Render compact RAG quality metrics for the answer card."""
    conf = meta["confidence"]
    conf_label = meta["confidence_label"].upper()
    source_relevance_score = meta.get("source_relevance", source_relevance(meta.get("citations", [])))
    response_time = meta.get("response_time_seconds", 5.6)
    citation_score = meta.get("citation_validity", citation_validity(meta.get("answer", ""), meta.get("citations", [])))

    if conf >= 0.8:
        conf_class = "conf-high"
    elif conf >= 0.6:
        conf_class = "conf-medium"
    else:
        conf_class = "conf-low"

    st.markdown(f"""
    <div class="metric-container">
        <div class="metric-item">
            <span class="metric-label">Độ tin cậy:</span>
            <span class="conf-badge {conf_class}">{conf:.0%} ({conf_label})</span>
        </div>
        <div class="metric-item">
            <span class="metric-label">Độ liên quan nguồn:</span>
            <span class="metric-value">{source_relevance_score:.0%}</span>
        </div>
        <div class="metric-item">
            <span class="metric-label">Thời gian phản hồi:</span>
            <span class="metric-value">{response_time:.1f}s</span>
        </div>
        <div class="metric-item">
            <span class="metric-label">Trích dẫn hợp lệ:</span>
            <span class="metric-value">{citation_score:.0%}</span>
        </div>
        <div class="metric-item">
            {badges_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Trợ lý Học tập Thông minh BAV",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium CSS styling injection
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title-container {
        padding: 1.5rem;
        background: linear-gradient(135deg, #1E3A8A 0%, #0F766E 100%);
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(30, 58, 138, 0.15);
        text-align: center;
    }
    
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        padding: 0;
        letter-spacing: -0.5px;
    }
    
    .main-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }
    
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1E3A8A;
        margin-bottom: 1rem;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 0.5rem;
    }
    
    .api-badge {
        padding: 0.4rem 0.8rem;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .api-success {
        background-color: #ECFDF5;
        color: #047857;
        border: 1px solid #A7F3D0;
    }
    
    .api-error {
        background-color: #FEF2F2;
        color: #B91C1C;
        border: 1px solid #FCA5A5;
    }
    
    .metric-container {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        margin: 0.75rem 0;
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        align-items: center;
    }
    
    .metric-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.85rem;
    }
    
    .metric-label {
        color: #64748B;
        font-weight: 500;
    }
    
    .metric-value {
        font-weight: 600;
    }
    
    .conf-badge {
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .conf-high {
        background-color: #D1FAE5;
        color: #065F46;
        border: 1px solid #A7F3D0;
    }
    .conf-medium {
        background-color: #FEF3C7;
        color: #92400E;
        border: 1px solid #FDE68A;
    }
    .conf-low {
        background-color: #FEE2E2;
        color: #991B1B;
        border: 1px solid #FCA5A5;
    }
    
    .metadata-tag {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid #E2E8F0;
    }
    .tag-subject {
        background-color: #EFF6FF;
        color: #1D4ED8;
        border-color: #BFDBFE;
    }
    .tag-doc {
        background-color: #F5F3FF;
        color: #6D28D9;
        border-color: #DDD6FE;
    }
    
    .citation-box {
        padding: 0.8rem;
        border-left: 4px solid #3B82F6;
        background: #F8FAFC;
        margin-bottom: 0.8rem;
        border-radius: 0 8px 8px 0;
    }
    
    .citation-header {
        display: flex;
        justify-content: space-between;
        font-size: 0.85rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 0.4rem;
    }
    
    .citation-score {
        color: #059669;
    }
    
    .citation-excerpt {
        font-style: italic;
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    .stChatMessage {
        border-radius: 12px;
        margin-bottom: 1rem;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- PERSISTENT CLIENT ID MANAGEMENT ---
client_id = get_client_id()

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = config.OPENAI_API_KEY or ""

if st.session_state.openai_api_key:
    config.OPENAI_API_KEY = st.session_state.openai_api_key

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.markdown('<div class="sidebar-header">🎓 Trợ Lý BAV AI</div>', unsafe_allow_html=True)
    
    if config.OPENAI_API_KEY:
        st.markdown(
            '<div class="api-badge api-success">🔑 <b>API Key:</b> Sẵn sàng sử dụng</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="api-badge api-error">⚠️ <b>API Key:</b> Chưa thiết lập</div>',
            unsafe_allow_html=True
        )
        
    api_key_input = st.text_input(
        "Cấu hình OpenAI API Key:",
        value=st.session_state.openai_api_key,
        type="password",
        placeholder="Nhập sk-...",
        help="Khóa API được sử dụng để gọi mô hình GPT để trả lời câu hỏi RAG. Nếu đã cấu hình file .env, khóa sẽ được tự động nhận diện."
    )
    
    if api_key_input != st.session_state.openai_api_key:
        st.session_state.openai_api_key = api_key_input
        config.OPENAI_API_KEY = api_key_input
        st.rerun()
        
    st.markdown("---")
    st.markdown("### ➕ Hội thoại mới")
    if st.button("➕ Tạo cuộc trò chuyện mới", use_container_width=True):
        new_id = str(uuid.uuid4())
        st.query_params["client_id"] = new_id
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 💬 Cuộc trò chuyện gần đây")
    sessions = list_available_sessions()
    if sessions:
        options = [s["id"] for s in sessions]
        labels = {s["id"]: s["title"] for s in sessions}
        
        current_id = client_id
        if current_id in options:
            default_index = options.index(current_id)
        else:
            options.insert(0, current_id)
            labels[current_id] = "💬 Phiên hiện tại (Đang chat)"
            default_index = 0
            
        selected_id = st.selectbox(
            "Chọn cuộc trò chuyện để xem lại:",
            options=options,
            index=default_index,
            format_func=lambda x: labels.get(x, x),
            key="session_selector"
        )
        
        if selected_id != current_id:
            st.query_params["client_id"] = selected_id
            st.session_state.messages = load_persisted_history(selected_id)
            st.rerun()
    else:
        st.caption("Chưa có cuộc trò chuyện nào trước đây.")
        
    st.markdown("---")
    st.markdown("### 🛠️ Tham số RAG (Mặc định)")
    st.caption("Các tham số đã được cấu hình tối ưu để trả lời chính xác dựa theo tài liệu chính thức.")
    st.write(f"- **Mô hình LLM**: `{config.LLM_MODEL}`")
    st.write(f"- **Embedding Model**: `{config.EMBEDDING_MODEL}`")
    st.write("- **Phương pháp**: `Semantic + Keyword Hybrid & Rerank`")
    st.write("- **Độ sáng tạo (Temperature)**: `0.1` (Tối ưu hóa độ chính xác thực tế)")
    st.write("- **Số lượng nguồn tối đa (Top K)**: `5` nguồn")
    
    st.markdown("---")
    if st.button("🗑️ Xóa lịch sử trò chuyện", use_container_width=True):
        st.session_state.messages = []
        save_persisted_history(client_id, [])
        st.rerun()
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("© 2026 BAV ITDE - Phiên bản RAG Chatbot Cao cấp")

# --- MAIN PAGE HEADER ---
st.markdown("""
<div class="main-title-container">
    <h1 class="main-title">🤖 Trợ Lý Học Tập BAV AI</h1>
    <p class="main-subtitle">Hỏi đáp quy chế đào tạo & nội dung môn học thông minh dựa trên tài liệu chính thống</p>
</div>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = load_persisted_history(client_id)

# --- RAG ANSWER HELPER WITH AUTO-DETECTION ---
def get_friendly_subject(subject_dir: str) -> str:
    """Return friendly Vietnamese subject name if mapped, else raw dir name."""
    return SUBJECT_MAP.get(subject_dir, subject_dir)

def process_rag_query(query_text: str):
    """Call the RAG answer_question module and process retrieved chunks to auto-detect metadata."""
    if not config.OPENAI_API_KEY:
        st.error("⚠️ Vui lòng cấu hình OpenAI API Key tại Sidebar trước khi hỏi.")
        return None

    started_at = time.perf_counter()
    with st.status("🔍 Đang xử lý câu hỏi...", expanded=True) as status:
        try:
            status.update(label="📁 Đang tìm kiếm tài liệu liên quan...", state="running")
            result = answer_question(
                question=query_text,
                top_k=5,
                temperature=0.1
            )
            
            status.update(label="🧠 Đang phân tích và tổng hợp câu trả lời...", state="running")
            
            detected_subjects = set()
            detected_docs = set()
            citations_data = []
            
            for chunk in result.retrieval.chunks:
                if chunk.subject_dir:
                    detected_subjects.add(get_friendly_subject(chunk.subject_dir))
                
                doc_name = chunk.source_file or "Tài liệu"
                detected_docs.add(doc_name.replace(".md", ""))
                    
                citations_data.append({
                    "rank": chunk.rank,
                    "title": doc_name,
                    "subject": get_friendly_subject(chunk.subject_dir) if chunk.subject_dir else "Học viện Ngân hàng",
                    "section": " > ".join(chunk.section_path) if chunk.section_path else "Mục chung",
                    "score": 1.0 / (1.0 + max(chunk.score, 0.0)),
                    "excerpt": chunk.text[:300] + ("..." if len(chunk.text) > 300 else ""),
                    "full_text": chunk.text,
                    "source_path": chunk.source_path
                })

            response_time = time.perf_counter() - started_at
            valid_citations = citation_validity(result.answer, citations_data)
            source_relevance_score = source_relevance(citations_data)

            status.update(label="✅ Xử lý hoàn tất!", state="complete", expanded=False)
            
            return {
                "question": query_text,
                "answer": result.answer,
                "confidence": result.confidence,
                "confidence_label": result.confidence_label,
                "source_relevance": source_relevance_score,
                "response_time_seconds": response_time,
                "citation_validity": valid_citations,
                "subjects": list(detected_subjects),
                "documents": list(detected_docs),
                "citations": citations_data
            }
            
        except Exception as e:
            status.update(label="❌ Có lỗi xảy ra!", state="error")
            st.error(f"Lỗi hệ thống: {str(e)}")
            return None

# --- STARTER QUESTIONS (EMPTY STATE) ---
if not st.session_state.messages:
    st.markdown("### 👋 Xin chào! Bạn muốn tìm hiểu thông tin gì hôm nay?")
    st.markdown("Tôi có thể hỗ trợ bạn tìm kiếm và trả lời chính xác các câu hỏi liên quan đến quy định học tập, quy chế đào tạo, hoặc nội dung các môn học Công nghệ Thông tin tại Học viện Ngân hàng.")
    st.markdown("Dưới đây là một số câu hỏi gợi ý bạn có thể tham khảo:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📜 Quy chế & Quy định BAV**")
        if st.button("Chuẩn đầu ra ngoại ngữ là gì?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Chuẩn đầu ra ngoại ngữ và CNTT của Học viện Ngân hàng là gì?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()
        if st.button("Quy chế tính điểm khuyên khích NCKH?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Quy định cộng điểm khuyến khích sinh viên nghiên cứu khoa học đạt giải như thế nào?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()
            
    with col2:
        st.markdown("**💻 Công nghệ & Lập trình**")
        if st.button("Cơ sở dữ liệu quan hệ?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Cơ sở dữ liệu quan hệ là gì và các khái niệm cơ bản?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()
        if st.button("Lập trình Hướng đối tượng?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Các đặc trưng cơ bản của lập trình hướng đối tượng trong Java?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()
            
    with col3:
        st.markdown("**🧠 Trí tuệ nhân tạo (AI)**")
        if st.button("Xử lý ngôn ngữ tự nhiên?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Xử lý ngôn ngữ tự nhiên là gì và các ứng dụng chính?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()
        if st.button("Mô hình Machine Learning?", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Quy trình xây dựng và đánh giá mô hình học máy (Machine Learning Pipeline) gồm các bước nào?"})
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(format_latex(msg["content"]))
        
        if msg["role"] == "assistant" and "rag_metadata" in msg:
            meta = msg["rag_metadata"]
            
            badges_html = ""
            if meta.get("citations"):
                primary_cite = meta["citations"][0]
                primary_subject = primary_cite["subject"]
                primary_doc = primary_cite["title"].replace(".md", "")
                badges_html += f'<span class="metadata-tag tag-subject">📚 Môn học: {primary_subject}</span> '
                badges_html += f'<span class="metadata-tag tag-doc">📄 Tài liệu: {primary_doc}</span> '
                
            render_rag_metrics(meta, badges_html)
            
            render_citations(meta["citations"], meta.get("question", ""))

# --- HANDLE NEW RAG PROCESSING (IF LAST MESSAGE IS USER) ---
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    user_query = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant"):
        rag_data = process_rag_query(user_query)
        if rag_data:
            st.markdown(format_latex(rag_data["answer"]))
            
            badges_html = ""
            if rag_data.get("citations"):
                primary_cite = rag_data["citations"][0]
                primary_subject = primary_cite["subject"]
                primary_doc = primary_cite["title"].replace(".md", "")
                badges_html += f'<span class="metadata-tag tag-subject">📚 Môn học: {primary_subject}</span> '
                badges_html += f'<span class="metadata-tag tag-doc">📄 Tài liệu: {primary_doc}</span> '
                
            render_rag_metrics(rag_data, badges_html)
            
            render_citations(rag_data["citations"], rag_data.get("question", ""))
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": rag_data["answer"],
                "rag_metadata": rag_data
            })
            save_persisted_history(client_id, st.session_state.messages)
            st.rerun()

# --- HANDLE NEW USER INPUT ---
if prompt := st.chat_input("Hãy đặt câu hỏi tại đây..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    save_persisted_history(client_id, st.session_state.messages)
    st.rerun()
