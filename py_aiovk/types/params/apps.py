from pydantic import BaseModel


class AppsIsNotificationsAllowedParams(BaseModel):
    user_id: int = None


class AppsSendRequestParams(BaseModel):
    user_id: int = None
    text: str = None
    type: str = None
    name: str = None
    key: str = None
    separate: bool = None


class AppsGetParams(BaseModel):
    app_id: int = None
    app_ids: str = None
    platform: str = None
    extended: bool = None
    return_friends: bool = None
    fields: str = None
    name_case: str = None
    app_fields: str = None


class AppsGetFriendsListParams(BaseModel):
    extended: bool = None
    count: int = None
    offset: int = None
    type: str = None
    fields: str = None


class AppsGetCatalogParams(BaseModel):
    sort: str = None
    offset: int = None
    count: int = None
    platform: str = None
    extended: bool = None
    return_friends: bool = None
    fields: str = None
    name_case: str = None
    q: str = None
    genre_id: int = None
    filter: str = None


class AppsGetScopesParams(BaseModel):
    type: str = None


