from aiohttp.web_app import Application
from aiohttp.web import run_app, Request, Response, json_response
from aiohttp.web_routedef import post
from pydantic import BaseModel

from py_aiovk.messages import Message


class CallbackClient(BaseModel):
    button_actions: list[str]
    keyboard: bool
    inline_keyboard: bool
    carousel: bool
    lang_id: int


class CallbackObject(BaseModel):
    message: Message
    client_info: CallbackClient


class CallbackRequest(BaseModel):
    group_id: int
    type: str
    event_id: str
    v: str
    object: CallbackObject
    secret: str


class Callback:
    def __init__(self, vk, code, secret):
        self.server = Application()
        self.code = code
        self.secret = secret
        self.vk = vk
        self.server.add_routes([post('/', self.handler)])
        self.handlers: dict = {}

    def add_handler(self, t, handler: list):
        if t in self.handlers:
            if handler is list:
                for h in handler:
                    self.handlers[t].append(h)
            else:
                self.handlers[t].append(handler)
        else:
            if handler is list:
                self.handlers.update({t: handler})
            else:
                self.handlers.update({t: [handler]})

    # TODO
    async def handler(self, request: Request):
        body = await request.json()
        if body['type'] == 'confirmation':
            group = await self.vk.group().get_by_id()
            code = await self.vk.group().get_callback_confirmation_code(group[0].id)
            return Response(text=code)

        body = CallbackRequest(**body)
        if self.secret != body.secret:
            return json_response({'error': 'Wrong secret'}, status=403)

        if body.type in self.handlers:
            for handler in self.handlers[body.type]:
                handler(body.object)

        return Response(text='ok')

    def run(self):
        run_app(self.server, loop=self.vk.loop)
