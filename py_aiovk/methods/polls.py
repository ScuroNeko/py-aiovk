from py_aiovk.types.params.polls import *


class Polls:
    def __init__(self, vk):
        self.vk = vk

    async def get_voters(self, params: PollsGetVotersParams):
        return await self.vk.execute('polls', 'getVoters', **params.model_dump(exclude_none=True))

    async def get_photo_upload_server(self, params: PollsGetPhotoUploadServerParams):
        return await self.vk.execute('polls', 'getPhotoUploadServer', **params.model_dump(exclude_none=True))

    async def save_photo(self, params: PollsSavePhotoParams):
        return await self.vk.execute('polls', 'savePhoto', **params.model_dump(exclude_none=True))

    async def create(self, params: PollsCreateParams):
        return await self.vk.execute('polls', 'create', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: PollsGetByIdParams):
        return await self.vk.execute('polls', 'getById', **params.model_dump(exclude_none=True))

