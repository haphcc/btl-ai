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

## 💻 Hướng dẫn sử dụng

Dự án hỗ trợ hai giao diện chính để tương tác với Chatbot: Giao diện dòng lệnh (CLI) và Giao diện Web (Streamlit).

> [!IMPORTANT]
> Đảm bảo bạn đã kích hoạt môi trường ảo (`venv`) và cấu hình đầy đủ file `.env` trước khi chạy các câu lệnh dưới đây.

### 1. Giao diện dòng lệnh (CLI)

Giao diện CLI hỗ trợ hai chế độ hoạt động:

#### Chế độ tương tác (Interactive Mode)
Chạy câu lệnh sau để mở chế độ trò chuyện liên tục trong terminal:
```bash
python src/rag_cli.py
```
*Nhập câu hỏi và nhấn **Enter**. Nhập `exit`, `quit` hoặc `q` để thoát.*

#### Chế độ hỏi đáp nhanh (Single Question Mode)
Bạn có thể gửi câu hỏi trực tiếp dưới dạng tham số dòng lệnh:
```bash
python src/rag_cli.py "Chuẩn đầu ra ngoại ngữ của Học viện Ngân hàng là gì?"
```

#### Các tùy chọn nâng cao hỗ trợ:
- `--show-context`: Hiển thị chi tiết nội dung các đoạn văn bản (context) đã được truy xuất để trả lời câu hỏi.
  ```bash
  python src/rag_cli.py "Quy chế điểm danh học phần?" --show-context
  ```
- `--json`: Trả về toàn bộ thông tin kết quả (bao gồm câu hỏi, câu trả lời, độ tin cậy, thông tin nguồn) dưới dạng định dạng JSON để phục vụ tích hợp.
  ```bash
  python src/rag_cli.py "Lập trình hướng đối tượng là gì?" --json
  ```
- `--top-k <số_lượng>`: Thay đổi số lượng đoạn văn bản tối đa cần truy xuất (mặc định là 5).
- `--temperature <giá_trị>`: Thiết lập độ sáng tạo của mô hình LLM (mặc định là 0.1).

---

### 2. Giao diện Web (Streamlit UI)

Giao diện Streamlit cung cấp trải nghiệm trò chuyện trực quan, hiển thị trực tiếp danh sách nguồn tài liệu tham khảo và mức độ tin cậy của câu trả lời.

Khởi động giao diện Web bằng câu lệnh sau:
```bash
streamlit run src/ui/app.py
```

Sau khi chạy lệnh, Streamlit sẽ tự động mở trình duyệt tại địa chỉ mặc định `http://localhost:8501`. Tại đây, bạn có thể:
- Nhập trực tiếp API Key OpenAI hoặc để trống nếu đã cấu hình trong file `.env`.
- Xem các câu hỏi gợi ý và lịch sử trò chuyện được tự động lưu trữ.
- Xem danh sách tài liệu trích dẫn chi tiết dưới dạng bảng hoặc các đoạn trích tiêu biểu theo thuật toán Hybrid Search.

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
