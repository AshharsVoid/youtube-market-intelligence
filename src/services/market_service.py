from api.sheets_client import SheetsClient
from api.youtube_client import YouTubeClient


class MarketService:

    def __init__(self):

        self.sheets = SheetsClient()
        self.youtube = YouTubeClient()

    def run(self):

        markets = self.sheets.read_sheet()

        for market in markets[:1]:
            query = f"{market['market']} {market['city']}"
            channels = self.youtube.search_channels(
                query=query,
                max_results=5
            )
            print(f"\nSearching: {query}")
            if channels:

                best_channel = channels[0]

                self.sheets.write_channel(
                    row=market["row"],
                    channel_name=best_channel["channel_name"],
                    channel_url=best_channel["url"]
                )
            for channel in channels:
                print(f"• {channel['channel_name']}")