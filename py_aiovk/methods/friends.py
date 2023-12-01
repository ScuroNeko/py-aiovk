from py_aiovk.types.params.friends import *


class Friends:
    def __init__(self, vk):
        self.vk = vk

    async def get_suggestions(self, params: FriendsGetSuggestionsParams):
        return await self.vk.execute('friends', 'getSuggestions', **params.model_dump(exclude_none=True))

    async def get_mutual(self, params: FriendsGetMutualParams):
        return await self.vk.execute('friends', 'getMutual', **params.model_dump(exclude_none=True))

    async def search(self, params: FriendsSearchParams):
        return await self.vk.execute('friends', 'search', **params.model_dump(exclude_none=True))

    async def get_lists(self, params: FriendsGetListsParams):
        return await self.vk.execute('friends', 'getLists', **params.model_dump(exclude_none=True))

    async def get(self, params: FriendsGetParams):
        return await self.vk.execute('friends', 'get', **params.model_dump(exclude_none=True))

    async def add(self, params: FriendsAddParams):
        return await self.vk.execute('friends', 'add', **params.model_dump(exclude_none=True))

    async def delete(self, params: FriendsDeleteParams):
        return await self.vk.execute('friends', 'delete', **params.model_dump(exclude_none=True))

    async def get_online(self, params: FriendsGetOnlineParams):
        return await self.vk.execute('friends', 'getOnline', **params.model_dump(exclude_none=True))

    async def add_list(self, params: FriendsAddListParams):
        return await self.vk.execute('friends', 'addList', **params.model_dump(exclude_none=True))

    async def delete_list(self, params: FriendsDeleteListParams):
        return await self.vk.execute('friends', 'deleteList', **params.model_dump(exclude_none=True))

    async def edit_list(self, params: FriendsEditListParams):
        return await self.vk.execute('friends', 'editList', **params.model_dump(exclude_none=True))

