from py_aiovk.types.params.donut import *


class Donut:
    def __init__(self, vk):
        self.vk = vk

    async def get_subscriptions(self, params: DonutGetSubscriptionsParams):
        return await self.vk.execute('donut', 'getSubscriptions', **params.model_dump(exclude_none=True))

    async def get_friends(self, params: DonutGetFriendsParams):
        return await self.vk.execute('donut', 'getFriends', **params.model_dump(exclude_none=True))

