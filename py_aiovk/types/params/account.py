from pydantic import BaseModel


class AccountSetSilenceModeParams(BaseModel):
    token: str = None
    device_id: str = None
    time: int = None
    chat_id: int = None
    user_id: int = None
    peer_id: int = None
    sound: int = None


class AccountUnbanParams(BaseModel):
    owner_id: int = None


class AccountGetInfoParams(BaseModel):
    fields: str = None


class AccountRegisterDeviceParams(BaseModel):
    token: str = None
    device_model: str = None
    device_year: int = None
    device_id: str = None
    system_version: str = None
    no_text: int = None
    subscribe: str = None
    settings: str = None
    sandbox: bool = None


class AccountUnregisterDeviceParams(BaseModel):
    token: str = None
    device_id: str = None
    sandbox: bool = None


class AccountSetOnlineParams(BaseModel):
    voip: bool = None


class AccountChangePasswordParams(BaseModel):
    restore_sid: str = None
    change_password_hash: str = None
    old_password: str = None
    new_password: str = None


class AccountGetBannedParams(BaseModel):
    offset: int = None
    count: int = None


class AccountGetCountersParams(BaseModel):
    filter: str = None


class AccountGetPushSettingsParams(BaseModel):
    token: str = None
    device_id: str = None


class AccountSaveProfileInfoParams(BaseModel):
    first_name: str = None
    last_name: str = None
    maiden_name: str = None
    screen_name: str = None
    cancel_request_id: int = None
    sex: int = None
    relation: int = None
    relation_partner_id: int = None
    bdate: str = None
    bdate_visibility: int = None
    home_town: str = None
    country_id: int = None
    city_id: int = None
    status: str = None


class AccountSetInfoParams(BaseModel):
    intro: int = None
    own_posts_default: bool = None
    no_wall_replies: bool = None
    name: str = None
    value: str = None


class AccountSetPushSettingsParams(BaseModel):
    device_id: str = None
    settings: str = None
    key: str = None
    value: str = None


