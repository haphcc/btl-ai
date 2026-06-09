import os

from dotenv import load_dotenv


load_dotenv()


from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", str(PROJECT_ROOT / "database" / "chroma_db"))
    CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "bav_itde_chunks")

    # Ingestion chunking defaults. Values are token estimates unless a tokenizer is added.
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "900"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))
    CHUNK_HARD_MAX = int(os.getenv("CHUNK_HARD_MAX", "1200"))

    # Models
    EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "openai")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    LLM_MODEL = os.getenv("LLM_MODEL_NAME", "gpt-4o-mini")


config = Config()
