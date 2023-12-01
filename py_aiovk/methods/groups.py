from py_aiovk.types.params.groups import *


class Groups:
    def __init__(self, vk):
        self.vk = vk

    async def get_members(self, params: GroupsGetMembersParams):
        return await self.vk.execute('groups', 'getMembers', **params.model_dump(exclude_none=True))

    async def edit(self, params: GroupsEditParams):
        return await self.vk.execute('groups', 'edit', **params.model_dump(exclude_none=True))

    async def is_member(self, params: GroupsIsMemberParams):
        return await self.vk.execute('groups', 'isMember', **params.model_dump(exclude_none=True))

    async def create(self, params: GroupsCreateParams):
        return await self.vk.execute('groups', 'create', **params.model_dump(exclude_none=True))

    async def get_invites(self, params: GroupsGetInvitesParams):
        return await self.vk.execute('groups', 'getInvites', **params.model_dump(exclude_none=True))

    async def search(self, params: GroupsSearchParams):
        return await self.vk.execute('groups', 'search', **params.model_dump(exclude_none=True))

    async def approve_request(self, params: GroupsApproveRequestParams):
        return await self.vk.execute('groups', 'approveRequest', **params.model_dump(exclude_none=True))

    async def get(self, params: GroupsGetParams):
        return await self.vk.execute('groups', 'get', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: GroupsGetByIdParams):
        return await self.vk.execute('groups', 'getById', **params.model_dump(exclude_none=True))

    async def get_addresses(self, params: GroupsGetAddressesParams):
        return await self.vk.execute('groups', 'getAddresses', **params.model_dump(exclude_none=True))

    async def invite(self, params: GroupsInviteParams):
        return await self.vk.execute('groups', 'invite', **params.model_dump(exclude_none=True))

    async def join(self, params: GroupsJoinParams):
        return await self.vk.execute('groups', 'join', **params.model_dump(exclude_none=True))

    async def leave(self, params: GroupsLeaveParams):
        return await self.vk.execute('groups', 'leave', **params.model_dump(exclude_none=True))

    async def remove_user(self, params: GroupsRemoveUserParams):
        return await self.vk.execute('groups', 'removeUser', **params.model_dump(exclude_none=True))

