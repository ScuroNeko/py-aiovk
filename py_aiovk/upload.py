import json

from aiohttp import FormData, ClientSession

from py_aiovk.attachments import load_attachments
from py_aiovk.types.params import PhotosGetMessagesUploadServerParams, DocsGetMessagesUploadServerParams
from py_aiovk.vk import VKClient


class JsonParser:
    @staticmethod
    def dumps(data):
        return json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
    def loads(string):
        return json.loads(string)


class VKUpload(object):
    __slots__ = ('vk',)

    def __init__(self, vk):
        if not isinstance(vk, VKClient):
            raise TypeError('The arg should be VKClient instance')

        self.vk = vk

    async def photo_messages(self, photo, pid=0):
        params = PhotosGetMessagesUploadServerParams(peer_id=pid)
        upload_info = await self.vk.photos().get_messages_upload_server(params=params)

        data = FormData()
        data.add_field(
            'photo', photo,
            content_type='multipart/form-data',
            filename='a.png',
        )

        async with ClientSession() as session, session.post(upload_info['upload_url'], data=data) as response:
            response = await response.text()
            response = json.loads(response)

        photos = await self.vk.photos().saveMessagesPhoto(**response)
        photos = [{'type': 'photo', 'photo': photo} for photo in photos]
        return load_attachments(photos)

    async def doc_message(self, doc, pid):
        params = DocsGetMessagesUploadServerParams(peer_id=pid)
        upload_info = await self.vk.docs().get_messages_upload_server(params)

        data = FormData()
        data.add_field(
            'file', doc,
            content_type='multipart/form-data',
            filename=f'a.png',
        )

        async with ClientSession() as session, session.post(upload_info['upload_url'], data=data) as response:
            response = await response.text()
            response = json.loads(response)

        return load_attachments([await self.vk.docs().save(**response)])
