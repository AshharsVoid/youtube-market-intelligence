from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import GOOGLE_SERVICE_ACCOUNT, GOOGLE_SHEET_ID


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

    def read_sheet(self):
        result = (
            self.service.spreadsheets()
            .values()
            .get(
                spreadsheetId=GOOGLE_SHEET_ID,
                range="Sheet2!A2:B"
            )
            .execute()
        )
        values = result.get("values", [])
        markets = []
        for row_number, row in enumerate(values, start=2):

            market_name = row[0] if len(row) > 0 else ""
            city = row[1] if len(row) > 1 else ""

            markets.append({
                "row": row_number,
                "market": market_name,
                "city": city
            })

        return markets
    def write_channel(self, row, channel_name, channel_url):

        body = {
         "values": [
                [channel_name, channel_url]
            ]
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=GOOGLE_SHEET_ID,
            range=f"Sheet2!C{row}:D{row}",
            valueInputOption="RAW",
            body=body
        ).execute()