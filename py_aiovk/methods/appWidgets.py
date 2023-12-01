from py_aiovk.types.params.appWidgets import *


class Appwidgets:
    def __init__(self, vk):
        self.vk = vk

    async def update(self, params: AppwidgetsUpdateParams):
        return await self.vk.execute('appWidgets', 'update', **params.model_dump(exclude_none=True))

