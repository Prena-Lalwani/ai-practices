import os
from pathlib import Path
from dotenv import load_dotenv

root_dir = Path(__file__).resolve().parent
load_dotenv(root_dir / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", 0.7))


def require_api_key() -> str:

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to .env")
    return OPENAI_API_KEY
