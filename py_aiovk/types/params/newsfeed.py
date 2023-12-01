from pydantic import BaseModel


class NewsfeedGetParams(BaseModel):
    filters: str = None
    return_banned: bool = None
    start_time: int = None
    end_time: int = None
    max_photos: int = None
    source_ids: str = None
    start_from: str = None
    count: int = None
    fields: str = None
    section: str = None


class NewsfeedAddBanParams(BaseModel):
    user_ids: str = None
    group_ids: str = None


class NewsfeedDeleteBanParams(BaseModel):
    user_ids: str = None
    group_ids: str = None


class NewsfeedGetSuggestedSourcesParams(BaseModel):
    offset: int = None
    count: int = None
    shuffle: bool = None
    fields: str = None


class NewsfeedGetCommentsParams(BaseModel):
    from: str = None
    count: int = None
    filters: str = None
    reposts: str = None
    start_time: int = None
    end_time: int = None
    last_comments: bool = None
    last_comments_count: int = None
    start_from: str = None
    fields: str = None


class NewsfeedUnignoreItemParams(BaseModel):
    type: str = None
    owner_id: int = None
    item_id: int = None
    track_code: str = None


class NewsfeedUnsubscribeParams(BaseModel):
    type: str = None
    owner_id: int = None
    item_id: int = None


