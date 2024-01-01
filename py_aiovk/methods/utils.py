from py_aiovk.types.params.utils import *


class Utils:
    def __init__(self, vk):
        self.vk = vk

    async def resolve_screen_name(self, params: UtilsResolveScreenNameParams):
        return await self.vk.execute('utils', 'resolveScreenName', **params.model_dump(exclude_none=True))

