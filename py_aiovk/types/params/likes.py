from pydantic import BaseModel


class LikesAddParams(BaseModel):
    type: str = None
    owner_id: int = None
    item_id: int = None
    access_key: str = None
    from_group: bool = None


class LikesDeleteParams(BaseModel):
    type: str = None
    owner_id: int = None
    item_id: int = None
    access_key: str = None
    from_group: bool = None


class LikesGetListParams(BaseModel):
    type: str = None
    owner_id: int = None
    item_id: int = None
    page_url: str = None
    filter: str = None
    friends_only: int = None
    extended: bool = None
    offset: int = None
    count: int = None
    skip_own: bool = None


