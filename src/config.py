from pathlib import Path
from dotenv import load_dotenv
import os

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env file explicitly
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError(
        f"YOUTUBE_API_KEY not found.\nExpected .env at: {dotenv_path}"
    )