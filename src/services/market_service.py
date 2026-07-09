from api.sheets_client import SheetsClient
from api.youtube_client import YouTubeClient
from ranking.channel_ranker import ChannelRanker


class MarketService:
<<<<<<< Updated upstream
=======
    """
    Coordinates the complete market intelligence workflow.
    """
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
        # Read all wholesale markets from Google Sheets
        markets = self.sheets.read_sheet()

        # Process each market
=======
        # Remove old results
        self.sheets.clear_channels()

        # Read all markets from Google Sheets
        markets = self.sheets.read_sheet()

        # Process every market
>>>>>>> Stashed changes
        for market in markets:

            market_name = market["market"]
            city = market["city"]

            query = f"{market_name} {city}"

            print("=" * 60)
            print(f"Searching: {query}")
            print("=" * 60)

<<<<<<< Updated upstream
=======
            # Search YouTube
>>>>>>> Stashed changes
            channels = self.youtube.search_channels(
                query=query,
                max_results=5
            )
<<<<<<< Updated upstream
=======

            # Rank channels
>>>>>>> Stashed changes
            channels = self.ranker.rank_channels(
                channels=channels,
                market=market_name,
                city=city
            )

<<<<<<< Updated upstream
            for index, channel in enumerate(channels, start=1):
                print(f"   Subscribers  : {channel.subscriber_count:,}")
                print(f"{index}. {channel.channel_name}")
                print(f"   Score        : {channel.score}")
=======
            # Save and display results
            for channel in channels:

                # Save to Google Sheets
                self.sheets.append_channel(
                    market=market,
                    channel=channel
                )

                # Console output
                print(f"{channel.rank}. {channel.channel_name}")
                print(f"   Score        : {channel.score}")
                print(f"   Subscribers  : {channel.subscriber_count:,}")
>>>>>>> Stashed changes
                print(f"   Videos       : {channel.video_count:,}")
                print(f"   Views        : {channel.view_count:,}")
                print(f"   Country      : {channel.country}")
                print(f"   Published    : {channel.published_at}")
<<<<<<< Updated upstream
=======
                print(f"   URL          : {channel.url}")
>>>>>>> Stashed changes
                print()