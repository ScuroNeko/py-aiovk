from pydantic import BaseModel
from typing import Union


class MessageType(BaseModel):
    id: int
    date: int
    peer_id: int


class Messages:
    def __init__(self, vk):
        self.vk = vk

    async def get_by_id(self, message_ids=Union[list[str, int], str]) -> MessageType:
        data = {}
        if message_ids is list[str]:
            data.update({'message_ids': ','.join(message_ids)})
        elif message_ids is list[int]:
            data.update({'message_ids': ','.join(map(str, message_ids))})
        else:
            data.update({'message_ids': message_ids})
        response = await self.vk.execute('getById', **data)
        return MessageType(**response)
