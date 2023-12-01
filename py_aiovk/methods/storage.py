from py_aiovk.types.params.storage import *


class Storage:
    def __init__(self, vk):
        self.vk = vk

    async def get(self, params: StorageGetParams):
        return await self.vk.execute('storage', 'get', **params.model_dump(exclude_none=True))

    async def get_keys(self, params: StorageGetKeysParams):
        return await self.vk.execute('storage', 'getKeys', **params.model_dump(exclude_none=True))

    async def set(self, params: StorageSetParams):
        return await self.vk.execute('storage', 'set', **params.model_dump(exclude_none=True))

