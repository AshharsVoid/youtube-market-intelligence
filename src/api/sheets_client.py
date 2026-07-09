from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import GOOGLE_SERVICE_ACCOUNT, GOOGLE_SHEET_ID


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


class SheetsClient:
    """
    Handles all communication with Google Sheets.
    """

    def __init__(self):
        """
        Create a Google Sheets API client.
        """

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
        """
        Read wholesale markets from Sheet2.

        Returns
        -------
        list[dict]
            List of markets.
        """

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

    def clear_channels(self):
        """
        Clear previous search results while keeping the header row.
        """

        self.service.spreadsheets().values().clear(
            spreadsheetId=GOOGLE_SHEET_ID,
            range="Channels!A2:J"
        ).execute()

    def append_channel(self, market, channel):
        """
        Append a ranked channel to the Channels sheet.

        Parameters
        ----------
        market : dict
            Market dictionary returned by read_sheet().

        channel : Channel
            Ranked Channel object.
        """

        body = {
            "values": [[
                market["market"],
                market["city"],
                channel.rank,
                channel.score,
                channel.channel_name,
                channel.subscriber_count,
                channel.video_count,
                channel.view_count,
                channel.country,
                channel.url
            ]]
        }

        self.service.spreadsheets().values().append(
            spreadsheetId=GOOGLE_SHEET_ID,
            range="Channels!A:J",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()