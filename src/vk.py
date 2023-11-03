from aiohttp import ClientSession
from asyncio import get_running_loop
from urllib.parse import urlencode

from pydantic import BaseModel

from src.messages import Messages


class VKError(BaseModel):
    error_code: int
    error_msg: str


class VKClient:
    def __init__(self, token):
        self.loop = get_running_loop()
        self.client = ClientSession(loop=self.loop)
        self.base_url = 'https://api.vk.com'
        self.version = '5.199'
        self.token = token

    async def close(self):
        await self.client.close()

    def __del__(self):
        self.loop.create_task(self.close())

    async def execute(self, method, **params) -> dict:
        url = f'{self.base_url}/method/{method}{urlencode(params)}'
        async with self.client.get(url) as r:
            response = await r.json()
            print(VKError(**(response['error'])))
        return {'id': 1, 'date': 1, 'peer_id': 1}

    def messages(self):
        return Messages(self)
