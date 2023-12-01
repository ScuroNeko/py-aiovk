from py_aiovk.types.params.podcasts import *


class Podcasts:
    def __init__(self, vk):
        self.vk = vk

    async def get_episodes(self, params: PodcastsGetEpisodesParams):
        return await self.vk.execute('podcasts', 'getEpisodes', **params.model_dump(exclude_none=True))

    async def get_episode(self, params: PodcastsGetEpisodeParams):
        return await self.vk.execute('podcasts', 'getEpisode', **params.model_dump(exclude_none=True))

    async def mark_as_listened(self, params: PodcastsMarkAsListenedParams):
        return await self.vk.execute('podcasts', 'markAsListened', **params.model_dump(exclude_none=True))

