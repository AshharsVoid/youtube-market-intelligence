from googleapiclient.discovery import build

from config import YOUTUBE_API_KEY


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

    def search_channels(self, query: str, max_results: int = 10):
        """
        Search YouTube for channels.

        Parameters
        ----------
        query : str
            Search keyword.

        max_results : int
            Maximum number of channels.

        Returns
        -------
        list
            List of channel dictionaries.
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

            channels.append({
                "channel_name": snippet["title"],
                "channel_id": snippet["channelId"],
                "description": snippet["description"],
                "url": f"https://www.youtube.com/channel/{snippet['channelId']}"
            })

        return channels