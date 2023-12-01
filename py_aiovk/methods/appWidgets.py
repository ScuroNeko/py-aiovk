from py_aiovk.types.params.appWidgets import *


class AppWidgets:
    def __init__(self, vk):
        self.vk = vk

    async def update(self, params: AppWidgetsUpdateParams):
        return await self.vk.execute('appWidgets', 'update', **params.model_dump(exclude_none=True))
