from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import GOOGLE_SERVICE_ACCOUNT


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


class SheetsClient:

    def __init__(self):

        credentials = Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT,
            scopes=SCOPES
        )

        self.service = build(
            "sheets",
            "v4",
            credentials=credentials
        )

        print("✅ Connected to Google Sheets!")