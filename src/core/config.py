import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./database/chroma_db")
    
    # TODO: Cấu hình tham số cho việc chia nhỏ văn bản (Ingestion)
    CHUNK_SIZE = None # TODO: Các thành viên chọn kích thước phù hợp (ví dụ 512, 1000)
    CHUNK_OVERLAP = None # TODO: Các thành viên chọn độ chồng lấp phù hợp (ví dụ 50, 100)
    
    # Models
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    LLM_MODEL = os.getenv("LLM_MODEL_NAME", "gpt-4o-mini")

config = Config()
