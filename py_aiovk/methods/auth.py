from py_aiovk.types.params.auth import *


class Auth:
    def __init__(self, vk):
        self.vk = vk

    async def check_phone(self, params: AuthCheckPhoneParams):
        return await self.vk.execute('auth', 'checkPhone',
                                     **params.model_dump(exclude_none=True))
