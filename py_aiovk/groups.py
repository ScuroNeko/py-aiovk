from typing import Union

from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str


class Groups:
    __slots__ = ('vk',)

    def __init__(self, vk):
        self.vk = vk

    async def execute(self, method, **params):
        return await self.vk.execute('groups', method, **params)

    async def get_by_id(self, group_ids: Union[str, list] = None) -> list[Group]:
        data = {}
        if group_ids is list:
            data.update({'message_ids': ','.join(map(str, group_ids))})
        elif group_ids is str:
            data.update({'message_ids': group_ids})

        response = await self.execute('getById', **data)
        return [Group(**group) for group in response['groups']]

    async def get_long_poll_server(self, group_id: int) -> dict:
        data = {'group_id': group_id}
        response = await self.execute('getLongPollServer', **data)
        return response

    async def get_callback_confirmation_code(self, group_id: int) -> str:
        data = {'group_id': group_id}
        response = await self.execute('getCallbackConfirmationCode', **data)
        return response['code']
