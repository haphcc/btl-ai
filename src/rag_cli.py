from __future__ import annotations

import sys
from pathlib import Path


if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.generation.rag_answer import main


if __name__ == "__main__":
    main()
