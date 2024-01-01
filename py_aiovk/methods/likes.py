from py_aiovk.types.params.likes import *


class Likes:
    def __init__(self, vk):
        self.vk = vk

    async def add(self, params: LikesAddParams):
        return await self.vk.execute('likes', 'add', **params.model_dump(exclude_none=True))

    async def delete(self, params: LikesDeleteParams):
        return await self.vk.execute('likes', 'delete', **params.model_dump(exclude_none=True))

    async def get_list(self, params: LikesGetListParams):
        return await self.vk.execute('likes', 'getList', **params.model_dump(exclude_none=True))

