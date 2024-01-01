from pydantic import BaseModel


class VideoGetParams(BaseModel):
    owner_id: int = None
    videos: str = None
    album_id: int = None
    count: int = None
    offset: int = None
    extended: bool = None
    fields: str = None
    sort_album: int = None


class VideoStopStreamingParams(BaseModel):
    group_id: int = None
    user_id: int = None
    video_id: int = None


class VideoGetAlbumsParams(BaseModel):
    owner_id: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    need_system: bool = None


class VideoGetLiveStatusParams(BaseModel):
    video_ids: str = None


class VideoCreateCommentParams(BaseModel):
    owner_id: int = None
    video_id: int = None
    message: str = None
    attachments: str = None
    from_group: bool = None
    reply_to_comment: int = None
    sticker_id: int = None
    guid: str = None
    track_code: str = None


class VideoEditParams(BaseModel):
    owner_id: int = None
    video_id: int = None
    name: str = None
    desc: str = None
    privacy_view: str = None
    privacy_comment: str = None
    no_comments: bool = None
    repeat: bool = None
    ord_info: str = None


class VideoAddParams(BaseModel):
    target_id: int = None
    video_id: int = None
    owner_id: int = None


class VideoAddAlbumParams(BaseModel):
    group_id: int = None
    title: str = None
    privacy: str = None


class VideoDeleteParams(BaseModel):
    video_id: int = None
    owner_id: int = None
    target_id: int = None


class VideoDeleteAlbumParams(BaseModel):
    group_id: int = None
    album_id: int = None


class VideoDeleteCommentParams(BaseModel):
    owner_id: int = None
    comment_id: int = None


class VideoEditAlbumParams(BaseModel):
    group_id: int = None
    album_id: int = None
    title: str = None
    privacy: str = None


class VideoGetAlbumByIdParams(BaseModel):
    owner_id: int = None
    album_id: int = None


class VideoGetCommentsParams(BaseModel):
    owner_id: int = None
    video_id: int = None
    need_likes: bool = None
    start_comment_id: int = None
    offset: int = None
    count: int = None
    sort: str = None
    extended: bool = None
    fields: str = None
    comment_id: int = None
    thread_items_count: int = None


class VideoGetLongPollServerParams(BaseModel):
    owner_id: int = None
    video_id: int = None


class VideoLiveAddBanParams(BaseModel):
    owners_ids: str = None


class VideoLiveDeleteBanParams(BaseModel):
    owners_ids: str = None


class VideoLiveSendGiftParams(BaseModel):
    owner_id: int = None
    video_id: int = None
    gift_id: int = None
    guid: str = None


class VideoRemoveFromAlbumParams(BaseModel):
    target_id: int = None
    album_id: int = None
    album_ids: str = None
    owner_id: int = None
    video_id: int = None


class VideoSaveParams(BaseModel):
    name: str = None
    description: str = None
    is_private: bool = None
    wallpost: bool = None
    link: str = None
    group_id: int = None
    album_id: int = None
    privacy_view: str = None
    privacy_comment: str = None
    no_comments: bool = None
    repeat: bool = None
    compression: bool = None


class VideoStartStreamingParams(BaseModel):
    video_id: int = None
    name: str = None
    description: str = None
    wallpost: bool = None
    group_id: int = None
    privacy_view: str = None
    privacy_comment: str = None
    no_comments: bool = None
    category_id: int = None
    publish: bool = None


