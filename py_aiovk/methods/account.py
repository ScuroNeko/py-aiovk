from py_aiovk.types.params.account import *


class Account:
    def __init__(self, vk):
        self.vk = vk

    async def set_silence_mode(self, params: AccountSetSilenceModeParams):
        return await self.vk.execute('account', 'setSilenceMode',
                                     **params.model_dump(exclude_none=True))

    async def unban(self, params: AccountUnbanParams):
        return await self.vk.execute('account', 'unban',
                                     **params.model_dump(exclude_none=True))

    async def get_info(self, params: AccountGetInfoParams):
        return await self.vk.execute('account', 'getInfo',
                                     **params.model_dump(exclude_none=True))

    async def register_device(self, params: AccountRegisterDeviceParams):
        return await self.vk.execute('account', 'registerDevice', **params.model_dump(exclude_none=True))

    async def unregister_device(self, params: AccountUnregisterDeviceParams):
        return await self.vk.execute('account', 'unregisterDevice', **params.model_dump(exclude_none=True))

    async def set_online(self, params: AccountSetOnlineParams):
        return await self.vk.execute('account', 'setOnline', **params.model_dump(exclude_none=True))

    async def change_password(self, params: AccountChangePasswordParams):
        return await self.vk.execute('account', 'changePassword', **params.model_dump(exclude_none=True))

    async def get_banned(self, params: AccountGetBannedParams):
        return await self.vk.execute('account', 'getBanned', **params.model_dump(exclude_none=True))

    async def get_counters(self, params: AccountGetCountersParams):
        return await self.vk.execute('account', 'getCounters', **params.model_dump(exclude_none=True))

    async def get_push_settings(self, params: AccountGetPushSettingsParams):
        return await self.vk.execute('account', 'getPushSettings', **params.model_dump(exclude_none=True))

    async def save_profile_info(self, params: AccountSaveProfileInfoParams):
        return await self.vk.execute('account', 'saveProfileInfo', **params.model_dump(exclude_none=True))

    async def set_info(self, params: AccountSetInfoParams):
        return await self.vk.execute('account', 'setInfo', **params.model_dump(exclude_none=True))

    async def set_push_settings(self, params: AccountSetPushSettingsParams):
        return await self.vk.execute('account', 'setPushSettings', **params.model_dump(exclude_none=True))
