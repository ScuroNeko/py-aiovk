from typing import Generator, AsyncIterable

from pydantic import BaseModel


class LongpollUpdate(BaseModel):
    group_id: int
    type: str
    event_id: str
    v: str
    object: dict


class Longpoll:
    __slots__ = ('vk', 'ts', 'key', 'server')

    def __init__(self, vk):
        self.vk = vk
        self.ts: str = ''
        self.key: str = ''
        self.server: str = ''

    async def init(self):
        group = await self.vk.group().get_by_id()
        lp = await self.vk.group().get_long_poll_server(group[0].id)

        self.ts = lp['ts']
        self.key = lp['key']
        self.server = lp['server']

    async def get_updates(self) -> list[LongpollUpdate]:
        url = f'{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait=25'
        async with self.vk.client.get(url) as r:
            response = await r.json()
            if 'failed' in response:
                failed = response['failed']
                match failed:
                    case 1:
                        self.ts = response['ts']
                        return await self.get_updates()
                    case 2, 3:
                        await self.init()
                        return await self.get_updates()
            self.ts = response['ts']
            return [LongpollUpdate(**update) for update in response['updates']]

    async def check(self) -> AsyncIterable[LongpollUpdate]:
        for update in await self.get_updates():
            yield update
