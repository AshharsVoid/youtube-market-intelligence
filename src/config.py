from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GOOGLE_SERVICE_ACCOUNT = os.getenv("GOOGLE_SERVICE_ACCOUNT")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found.")

if not GOOGLE_SERVICE_ACCOUNT:
    raise ValueError("GOOGLE_SERVICE_ACCOUNT not found.")

if not GOOGLE_SHEET_ID:
    raise ValueError("GOOGLE_SHEET_ID not found.")