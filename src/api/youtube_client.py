from googleapiclient.discovery import build

from config import YOUTUBE_API_KEY
from models.channel import Channel


class YouTubeClient:
    """
    Handles communication with the YouTube Data API.
    """

    def __init__(self):
        """
        Create a YouTube API client.
        """
        self.youtube = build(
            serviceName="youtube",
            version="v3",
            developerKey=YOUTUBE_API_KEY
        )

    def search_channels(self, query: str, max_results: int = 10) -> list[Channel]:
        """
        Search YouTube for channels and enrich them with statistics.

        Parameters
        ----------
        query : str
            Search keyword.

        max_results : int
            Maximum number of channels to return.

        Returns
        -------
        list[Channel]
            Fully populated Channel objects.
        """

        request = self.youtube.search().list(
            part="snippet",
            q=query,
            type="channel",
            maxResults=max_results
        )

        response = request.execute()

        channels = []

        for item in response["items"]:

            snippet = item["snippet"]

            channel = Channel(
                channel_name=snippet["title"],
                channel_id=snippet["channelId"],
                description=snippet.get("description", ""),
                url=f"https://www.youtube.com/channel/{snippet['channelId']}"
            )

            # Populate subscriber count, views, etc.
            self.enrich_channel(channel)

            channels.append(channel)

        return channels

    def enrich_channel(self, channel: Channel) -> None:
        """
        Fetch additional metadata for a channel and update the Channel object.

        Parameters
        ----------
        channel : Channel
            Channel object to enrich.
        """

        request = self.youtube.channels().list(
            part="statistics,snippet",
            id=channel.channel_id
        )

        response = request.execute()

        if not response["items"]:
            return

        item = response["items"][0]

        statistics = item["statistics"]
        snippet = item["snippet"]

        channel.subscriber_count = int(
            statistics.get("subscriberCount", 0)
        )

        channel.video_count = int(
            statistics.get("videoCount", 0)
        )

        channel.view_count = int(
            statistics.get("viewCount", 0)
        )

        channel.country = snippet.get("country", "")

        channel.published_at = snippet.get(
            "publishedAt",
            ""
        )