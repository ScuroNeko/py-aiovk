from py_aiovk.types.params.docs import *


class Docs:
    def __init__(self, vk):
        self.vk = vk

    async def get_upload_server(self, params: DocsGetUploadServerParams):
        return await self.vk.execute('docs', 'getUploadServer', **params.model_dump(exclude_none=True))

    async def add(self, params: DocsAddParams):
        return await self.vk.execute('docs', 'add', **params.model_dump(exclude_none=True))

    async def delete(self, params: DocsDeleteParams):
        return await self.vk.execute('docs', 'delete', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: DocsGetByIdParams):
        return await self.vk.execute('docs', 'getById', **params.model_dump(exclude_none=True))

    async def get(self, params: DocsGetParams):
        return await self.vk.execute('docs', 'get', **params.model_dump(exclude_none=True))

    async def save(self, params: DocsSaveParams):
        return await self.vk.execute('docs', 'save', **params.model_dump(exclude_none=True))

    async def search(self, params: DocsSearchParams):
        return await self.vk.execute('docs', 'search', **params.model_dump(exclude_none=True))

