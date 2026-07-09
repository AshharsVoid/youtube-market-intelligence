class ChannelRanker:
    """
    Responsible for scoring and ranking YouTube channels.
    """

    def score_channel(
        self,
        channel,
        market,
        city
    ):
        """
        Calculate a relevance score for a channel.
        """

        score = 0

        name = channel.channel_name.lower()
        description = channel.description.lower()

        market = market.lower()
        city = city.lower()

        # Market name in channel name
        if market in name:
            score += 40

        # City in channel name
        if city in name:
            score += 20

        # Common wholesale keywords
        if "mandi" in name:
            score += 10

        if "apmc" in name:
            score += 10

        # Market mentioned in description
        if market in description:
            score += 10

        # Channel quality signals
        if channel.subscriber_count > 10_000:
            score += 5

        if channel.video_count > 100:
            score += 5

        channel.score = score

        return score

    def rank_channels(
        self,
        channels,
        market,
        city
    ):
        """
        Score every channel and return them sorted by score.
        """

        for channel in channels:
            self.score_channel(
                channel,
                market,
                city
            )

        channels.sort(
            key=lambda c: c.score,
            reverse=True
        )

        for index, channel in enumerate(channels, start=1):
            channel.rank = index

        return channels