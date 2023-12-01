from py_aiovk.types.params.wall import *


class Wall:
    def __init__(self, vk):
        self.vk = vk

    async def delete_comment(self, params: WallDeleteCommentParams):
        return await self.vk.execute('wall', 'deleteComment', **params.model_dump(exclude_none=True))

    async def delete(self, params: WallDeleteParams):
        return await self.vk.execute('wall', 'delete', **params.model_dump(exclude_none=True))

    async def close_comments(self, params: WallCloseCommentsParams):
        return await self.vk.execute('wall', 'closeComments', **params.model_dump(exclude_none=True))

    async def edit(self, params: WallEditParams):
        return await self.vk.execute('wall', 'edit', **params.model_dump(exclude_none=True))

    async def open_comments(self, params: WallOpenCommentsParams):
        return await self.vk.execute('wall', 'openComments', **params.model_dump(exclude_none=True))

    async def post(self, params: WallPostParams):
        return await self.vk.execute('wall', 'post', **params.model_dump(exclude_none=True))

    async def repost(self, params: WallRepostParams):
        return await self.vk.execute('wall', 'repost', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: WallGetByIdParams):
        return await self.vk.execute('wall', 'getById', **params.model_dump(exclude_none=True))

    async def check_copyright_link(self, params: WallCheckCopyrightLinkParams):
        return await self.vk.execute('wall', 'checkCopyrightLink', **params.model_dump(exclude_none=True))

    async def search(self, params: WallSearchParams):
        return await self.vk.execute('wall', 'search', **params.model_dump(exclude_none=True))

    async def get(self, params: WallGetParams):
        return await self.vk.execute('wall', 'get', **params.model_dump(exclude_none=True))

    async def get_comment(self, params: WallGetCommentParams):
        return await self.vk.execute('wall', 'getComment', **params.model_dump(exclude_none=True))

    async def parse_attached_link(self, params: WallParseAttachedLinkParams):
        return await self.vk.execute('wall', 'parseAttachedLink', **params.model_dump(exclude_none=True))

