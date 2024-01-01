from py_aiovk.types.params.search import *


class Search:
    def __init__(self, vk):
        self.vk = vk

    async def get_hints(self, params: SearchGetHintsParams):
        return await self.vk.execute('search', 'getHints', **params.model_dump(exclude_none=True))

