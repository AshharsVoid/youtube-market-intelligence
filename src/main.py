from api.youtube_client import YouTubeClient


def main():

    print("=" * 50)
    print("YouTube Market Intelligence")
    print("=" * 50)

    market = "Azadpur Mandi"

    print(f"\nSearching for: {market}\n")

    client = YouTubeClient()

    channels = client.search_channels(market)

    print(f"Found {len(channels)} channels\n")

    for index, channel in enumerate(channels, start=1):

        print(f"{index}. {channel['channel_name']}")
        print(f"   {channel['url']}")
        print()


if __name__ == "__main__":
    main()