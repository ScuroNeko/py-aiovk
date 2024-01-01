from pydantic import BaseModel


class FriendsGetSuggestionsParams(BaseModel):
    filter: str = None
    count: int = None
    offset: int = None
    fields: str = None
    name_case: str = None


class FriendsGetMutualParams(BaseModel):
    source_uid: int = None
    target_uid: int = None
    target_uids: str = None
    order: str = None
    count: int = None
    offset: int = None


class FriendsSearchParams(BaseModel):
    user_id: int = None
    q: str = None
    fields: str = None
    name_case: str = None
    offset: int = None
    count: int = None


class FriendsGetListsParams(BaseModel):
    user_id: int = None
    return_system: bool = None


class FriendsGetParams(BaseModel):
    user_id: int = None
    order: str = None
    list_id: int = None
    count: int = None
    offset: int = None
    fields: str = None
    name_case: str = None
    ref: str = None


class FriendsAddParams(BaseModel):
    user_id: int = None
    text: str = None
    follow: bool = None


class FriendsDeleteParams(BaseModel):
    user_id: int = None


class FriendsGetOnlineParams(BaseModel):
    user_id: int = None
    list_id: int = None
    online_mobile: bool = None
    order: str = None
    count: int = None
    offset: int = None


class FriendsAddListParams(BaseModel):
    name: str = None
    user_ids: str = None


class FriendsDeleteListParams(BaseModel):
    list_id: str = None


class FriendsEditListParams(BaseModel):
    name: str = None
    list_id: str = None
    user_ids: str = None
    add_user_ids: str = None
    delete_user_ids: str = None


