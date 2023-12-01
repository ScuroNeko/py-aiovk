from py_aiovk.types.params.stories import *


class Stories:
    def __init__(self, vk):
        self.vk = vk

    async def get_photo_upload_server(self, params: StoriesGetPhotoUploadServerParams):
        return await self.vk.execute('stories', 'getPhotoUploadServer', **params.model_dump(exclude_none=True))

    async def get_video_upload_server(self, params: StoriesGetVideoUploadServerParams):
        return await self.vk.execute('stories', 'getVideoUploadServer', **params.model_dump(exclude_none=True))

    async def hide_all_replies(self, params: StoriesHideAllRepliesParams):
        return await self.vk.execute('stories', 'hideAllReplies', **params.model_dump(exclude_none=True))

    async def hide_reply(self, params: StoriesHideReplyParams):
        return await self.vk.execute('stories', 'hideReply', **params.model_dump(exclude_none=True))

    async def get(self, params: StoriesGetParams):
        return await self.vk.execute('stories', 'get', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: StoriesGetByIdParams):
        return await self.vk.execute('stories', 'getById', **params.model_dump(exclude_none=True))

    async def get_stats(self, params: StoriesGetStatsParams):
        return await self.vk.execute('stories', 'getStats', **params.model_dump(exclude_none=True))

    async def get_viewers(self, params: StoriesGetViewersParams):
        return await self.vk.execute('stories', 'getViewers', **params.model_dump(exclude_none=True))

    async def save(self, params: StoriesSaveParams):
        return await self.vk.execute('stories', 'save', **params.model_dump(exclude_none=True))

