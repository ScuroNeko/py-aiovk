from pydantic import BaseModel


class WallDeleteCommentParams(BaseModel):
    owner_id: int = None
    comment_id: int = None


class WallDeleteParams(BaseModel):
    owner_id: int = None
    post_id: int = None


class WallCloseCommentsParams(BaseModel):
    owner_id: int = None
    post_id: int = None


class WallEditParams(BaseModel):
    owner_id: int = None
    post_id: int = None
    friends_only: bool = None
    message: str = None
    attachments: str = None
    services: str = None
    signed: bool = None
    publish_date: int = None
    lat: str = None
    long: str = None
    place_id: int = None
    mark_as_ads: bool = None
    close_comments: bool = None
    donut_paid_duration: int = None
    poster_bkg_id: int = None
    poster_bkg_owner_id: int = None
    poster_bkg_access_hash: str = None
    copyright: str = None


class WallOpenCommentsParams(BaseModel):
    owner_id: int = None
    post_id: int = None


class WallPostParams(BaseModel):
    owner_id: int = None
    friends_only: bool = None
    from_group: bool = None
    message: str = None
    attachments: str = None
    services: str = None
    signed: bool = None
    publish_date: int = None
    lat: str = None
    long: str = None
    place_id: int = None
    post_id: int = None
    guid: str = None
    mark_as_ads: bool = None
    link_title: str = None
    link_photo_id: str = None
    close_comments: bool = None
    donut_paid_duration: int = None
    mute_notifications: bool = None
    copyright: str = None


class WallRepostParams(BaseModel):
    object: str = None
    message: str = None
    group_id: int = None
    mark_as_ads: bool = None
    mute_notifications: bool = None


class WallGetByIdParams(BaseModel):
    posts: str = None
    extended: bool = None
    copy_history_depth: int = None
    fields: str = None


class WallCheckCopyrightLinkParams(BaseModel):
    link: str = None


class WallSearchParams(BaseModel):
    owner_id: int = None
    domain: str = None
    query: str = None
    owners_only: bool = None
    count: int = None
    offset: int = None
    extended: bool = None
    fields: str = None


class WallGetParams(BaseModel):
    owner_id: int = None
    domain: str = None
    offset: int = None
    count: int = None
    filter: str = None
    extended: bool = None
    fields: str = None


class WallGetCommentParams(BaseModel):
    owner_id: int = None
    comment_id: int = None
    extended: bool = None
    fields: str = None


class WallParseAttachedLinkParams(BaseModel):
    links: str = None
    extended: bool = None
    fields: str = None
    name_case: str = None


