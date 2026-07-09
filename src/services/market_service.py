from api.sheets_client import SheetsClient
from api.youtube_client import YouTubeClient
from ranking.channel_ranker import ChannelRanker


class MarketService:

    def __init__(self):
        """
        Initialize all services.
        """
        self.sheets = SheetsClient()
        self.youtube = YouTubeClient()
        self.ranker = ChannelRanker()

    def run(self):
        """
        Main application workflow.
        """

        # Read all wholesale markets from Google Sheets
        markets = self.sheets.read_sheet()

        # Process each market
        for market in markets:

            market_name = market["market"]
            city = market["city"]

            query = f"{market_name} {city}"

            print("=" * 60)
            print(f"Searching: {query}")
            print("=" * 60)

            channels = self.youtube.search_channels(
                query=query,
                max_results=5
            )
            channels = self.ranker.rank_channels(
                channels=channels,
                market=market_name,
                city=city
            )

            for index, channel in enumerate(channels, start=1):
                print(f"   Subscribers  : {channel.subscriber_count:,}")
                print(f"{index}. {channel.channel_name}")
                print(f"   Score        : {channel.score}")
                print(f"   Videos       : {channel.video_count:,}")
                print(f"   Views        : {channel.view_count:,}")
                print(f"   Country      : {channel.country}")
                print(f"   Published    : {channel.published_at}")
                print()