from py_aiovk.types.params.status import *


class Status:
    def __init__(self, vk):
        self.vk = vk

    async def set(self, params: StatusSetParams):
        return await self.vk.execute('status', 'set', **params.model_dump(exclude_none=True))

