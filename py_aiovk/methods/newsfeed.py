from py_aiovk.types.params.newsfeed import *


class Newsfeed:
    def __init__(self, vk):
        self.vk = vk

    async def get(self, params: NewsfeedGetParams):
        return await self.vk.execute('newsfeed', 'get', **params.model_dump(exclude_none=True))

    async def add_ban(self, params: NewsfeedAddBanParams):
        return await self.vk.execute('newsfeed', 'addBan', **params.model_dump(exclude_none=True))

    async def delete_ban(self, params: NewsfeedDeleteBanParams):
        return await self.vk.execute('newsfeed', 'deleteBan', **params.model_dump(exclude_none=True))

    async def get_suggested_sources(self, params: NewsfeedGetSuggestedSourcesParams):
        return await self.vk.execute('newsfeed', 'getSuggestedSources', **params.model_dump(exclude_none=True))

    async def get_comments(self, params: NewsfeedGetCommentsParams):
        return await self.vk.execute('newsfeed', 'getComments', **params.model_dump(exclude_none=True))

    async def unignore_item(self, params: NewsfeedUnignoreItemParams):
        return await self.vk.execute('newsfeed', 'unignoreItem', **params.model_dump(exclude_none=True))

    async def unsubscribe(self, params: NewsfeedUnsubscribeParams):
        return await self.vk.execute('newsfeed', 'unsubscribe', **params.model_dump(exclude_none=True))

