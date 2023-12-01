from pydantic import BaseModel


class StoriesGetPhotoUploadServerParams(BaseModel):
    add_to_news: bool = None
    user_ids: str = None
    reply_to_story: str = None
    link_text: str = None
    link_url: str = None
    group_id: int = None
    clickable_stickers: str = None


class StoriesGetVideoUploadServerParams(BaseModel):
    add_to_news: bool = None
    user_ids: str = None
    reply_to_story: str = None
    link_text: str = None
    link_url: str = None
    group_id: int = None
    clickable_stickers: str = None


class StoriesHideAllRepliesParams(BaseModel):
    owner_id: int = None
    group_id: int = None


class StoriesHideReplyParams(BaseModel):
    owner_id: int = None
    story_id: int = None


class StoriesGetParams(BaseModel):
    owner_id: int = None
    extended: bool = None
    fields: str = None


class StoriesGetByIdParams(BaseModel):
    stories: str = None
    extended: bool = None
    fields: str = None


class StoriesGetStatsParams(BaseModel):
    owner_id: int = None
    story_id: int = None


class StoriesGetViewersParams(BaseModel):
    owner_id: int = None
    story_id: int = None
    count: int = None
    offset: int = None
    extended: bool = None


class StoriesSaveParams(BaseModel):
    upload_results: str = None
    extended: bool = None
    fields: str = None


