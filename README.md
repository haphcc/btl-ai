# 🤖 RAG Chatbot - BTL Trí tuệ nhân tạo

Dự án xây dựng hệ thống Chatbot hỏi đáp thông tin trường học và tài liệu môn học dựa trên kỹ thuật **Retrieval-Augmented Generation (RAG)**.

## 📁 Cấu trúc thư mục

- `data/`: Lưu trữ dữ liệu đầu vào.
  - `raw/`: Các file PDF, Docx, slide bài giảng gốc.
  - `processed/`: Dữ liệu sau khi được chuyển đổi sang định dạng Markdown/Cleaned text.
- `database/`: Lưu trữ cơ sở dữ liệu vector (ChromaDB, SQLite, ...).
- `src/`: Mã nguồn chính của dự án.
  - `core/`: Cấu hình hệ thống, quản lý LLM và Embedding model.
  - `ingestion/`: Các script xử lý dữ liệu (Extract, Chunking, Embedding, Upsert).
  - `retrieval/`: Logic tìm kiếm thông tin liên quan (Hybrid search, Reranking).
  - `ui/`: Giao diện người dùng (Streamlit).
- `notebooks/`: Các file Jupyter Notebook để thử nghiệm chunking và prompt.
- `tests/`: Kịch bản kiểm thử và đánh giá mô hình (RAGAS).

## 🚀 Hướng dẫn cài đặt

1. **Clone repository:**
   ```bash
   git clone <url-github-cua-nhom>
   cd BTL-AI
   ```

2. **Tạo môi trường ảo:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Cấu hình môi trường:**
   - Sao chép file `.env.example` thành `.env`.
   - Điền các API Key cần thiết (OpenAI, Gemini, hoặc cấu hình local model).

## 🛠 Lộ trình thực hiện (Dựa trên OUTLINE)

1. [ ] Thu thập tài liệu (PDF, slide, văn bản trường).
2. [ ] Xây dựng module Ingestion (Chuyển đổi sang Markdown, cắt nhỏ văn bản).
3. [ ] Cài đặt Vector Database và Embedding.
4. [ ] Phát triển logic Retrieval (Tìm kiếm ngữ nghĩa).
5. [ ] Xây dựng Prompt và kết nối LLM (GPT-4, Gemini hoặc Llama 3).
6. [ ] Đánh giá độ chính xác (Evaluation).
7. [ ] Hoàn thiện giao diện Demo.

## 👥 Thành viên nhóm
- Thành viên 1: ...
- Thành viên 2: ...
- Thành viên 3: ...
