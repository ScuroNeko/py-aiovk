from py_aiovk.types.params.apps import *


class Apps:
    def __init__(self, vk):
        self.vk = vk

    async def is_notifications_allowed(self, params: AppsIsNotificationsAllowedParams):
        return await self.vk.execute('apps', 'isNotificationsAllowed', **params.model_dump(exclude_none=True))

    async def send_request(self, params: AppsSendRequestParams):
        return await self.vk.execute('apps', 'sendRequest', **params.model_dump(exclude_none=True))

    async def get(self, params: AppsGetParams):
        return await self.vk.execute('apps', 'get', **params.model_dump(exclude_none=True))

    async def get_friends_list(self, params: AppsGetFriendsListParams):
        return await self.vk.execute('apps', 'getFriendsList', **params.model_dump(exclude_none=True))

    async def get_catalog(self, params: AppsGetCatalogParams):
        return await self.vk.execute('apps', 'getCatalog', **params.model_dump(exclude_none=True))

    async def get_scopes(self, params: AppsGetScopesParams):
        return await self.vk.execute('apps', 'getScopes', **params.model_dump(exclude_none=True))

