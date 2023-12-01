from py_aiovk.types.params.users import *


class Users:
    def __init__(self, vk):
        self.vk = vk

    async def get_followers(self, params: UsersGetFollowersParams):
        return await self.vk.execute('users', 'getFollowers', **params.model_dump(exclude_none=True))

    async def get_subscriptions(self, params: UsersGetSubscriptionsParams):
        return await self.vk.execute('users', 'getSubscriptions', **params.model_dump(exclude_none=True))

    async def get(self, params: UsersGetParams):
        return await self.vk.execute('users', 'get', **params.model_dump(exclude_none=True))

    async def search(self, params: UsersSearchParams):
        return await self.vk.execute('users', 'search', **params.model_dump(exclude_none=True))

