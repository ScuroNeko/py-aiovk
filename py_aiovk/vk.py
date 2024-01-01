from asyncio import get_running_loop, new_event_loop, set_event_loop
from urllib.parse import urlencode

from aiohttp import ClientSession

from py_aiovk.methods import Account, Apps, AppWidgets, Audio, Auth, Board, \
    Database, Docs, Donut, Fave, Friends, Groups, Likes, Market, Messages, \
    Newsfeed, Notes, Photos, Podcasts, Polls, Search, Status, Storage, Store, \
    Stories, Users, Utils, Video, Wall
from py_aiovk.callback import Callback
from py_aiovk.longpoll import Longpoll


class VKException(Exception):
    def __init__(self, error):
        self.error_code = error['error_code']
        self.error_msg = error['error_msg']
        super().__init__(self.error_msg)


class VKClient:
    def __init__(self, token, version='5.199'):
        try:
            self.loop = get_running_loop()
        except RuntimeError:
            self.loop = new_event_loop()

        set_event_loop(self.loop)
        self.client = ClientSession(loop=self.loop)
        self.base_url = 'https://api.vk.com'
        self.version = version
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

    def account(self):
        return Account(self)

    def apps(self):
        return Apps(self)

    def app_widget(self):
        return AppWidgets(self)

    def audio(self):
        return Audio(self)

    def auth(self):
        return Auth(self)

    def board(self):
        return Board(self)

    def database(self):
        return Database(self)

    def docs(self):
        return Docs(self)

    def donut(self):
        return Donut(self)

    def fave(self):
        return Fave(self)

    def friends(self):
        return Friends(self)

    def groups(self):
        return Groups(self)

    def likes(self):
        return Likes(self)

    def market(self):
        return Market(self)

    def messages(self):
        return Messages(self)

    def newsfeed(self):
        return Newsfeed(self)

    def notes(self):
        return Notes(self)

    def photos(self):
        return Photos(self)

    def podcasts(self):
        return Podcasts(self)

    def polls(self):
        return Polls(self)

    def search(self):
        return Search(self)

    def status(self):
        return Status(self)

    def storage(self):
        return Storage(self)

    def store(self):
        return Store(self)

    def stories(self):
        return Stories(self)

    def users(self):
        return Users(self)

    def utils(self):
        return Utils(self)

    def video(self):
        return Video(self)

    def wall(self):
        return Wall(self)

    # Service
    def callback(self, code, secret=''):
        return Callback(self, code, secret)

    def longpoll(self):
        return Longpoll(self)
