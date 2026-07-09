from dataclasses import dataclass


@dataclass
class Channel:

    channel_name: str
    channel_id: str
    description: str
    url: str

    subscriber_count: int = 0
    video_count: int = 0
    view_count: int = 0

    country: str = ""
    published_at: str = ""

    score: int = 0