from pydantic import BaseModel


class PodcastsGetEpisodesParams(BaseModel):
    owner_id: int = None
    count: int = None
    offset: int = None
    order: str = None


class PodcastsGetEpisodeParams(BaseModel):
    owner_id: int = None
    episode_id: int = None


class PodcastsMarkAsListenedParams(BaseModel):
    owner_id: int = None
    episode_id: int = None
    ref: str = None


