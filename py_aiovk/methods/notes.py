from py_aiovk.types.params.notes import *


class Notes:
    def __init__(self, vk):
        self.vk = vk

    async def get_by_id(self, params: NotesGetByIdParams):
        return await self.vk.execute('notes', 'getById', **params.model_dump(exclude_none=True))

