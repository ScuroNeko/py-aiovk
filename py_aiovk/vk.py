from asyncio import get_running_loop, new_event_loop, set_event_loop
from urllib.parse import urlencode

from aiohttp import ClientSession

from py_aiovk.callback import Callback
from py_aiovk.groups import Groups
from py_aiovk.longpoll import Longpoll
from py_aiovk.messages import Messages


class VKException(Exception):
    def __init__(self, error):
        self.error_code = error['error_code']
        self.error_msg = error['error_msg']
        super().__init__(self.error_msg)


class VKClient:
    def __init__(self, token):
        try:
            self.loop = get_running_loop()
        except RuntimeError:
            self.loop = new_event_loop()

        set_event_loop(self.loop)
        self.client = ClientSession(loop=self.loop)
        self.base_url = 'https://api.vk.com'
        self.version = '5.199'
        self.token = token

    async def close(self):
        if not self.client.closed:
            await self.client.close()

    def __del__(self):
        self.loop.create_task(self.close())

    async def execute(self, category, method, **params) -> dict:
        params.update({'access_token': self.token, 'v': self.version})
        url = f'{self.base_url}/method/{category}.{method}?{urlencode(params)}'
        async with self.client.get(url) as r:
            response = await r.json()
            if 'error' in response:
                raise VKException(response['error'])
        return response['response']

    def messages(self):
        return Messages(self)

    def group(self):
        return Groups(self)

    def callback(self, code, secret=''):
        return Callback(self, code, secret)

    def longpoll(self):
        return Longpoll(self)
