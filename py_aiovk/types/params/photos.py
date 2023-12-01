from pydantic import BaseModel


class PhotosGetChatUploadServerParams(BaseModel):
    chat_id: int = None
    crop_x: int = None
    crop_y: int = None
    crop_width: int = None


class PhotosGetOwnerCoverPhotoUploadServerParams(BaseModel):
    group_id: int = None
    crop_x: int = None
    crop_y: int = None
    crop_x2: int = None
    crop_y2: int = None


class PhotosGetWallUploadServerParams(BaseModel):
    group_id: int = None


class PhotosSaveMarketAlbumPhotoParams(BaseModel):
    group_id: int = None
    photo: str = None
    server: int = None
    hash: str = None


class PhotosSaveOwnerCoverPhotoParams(BaseModel):
    hash: str = None
    photo: str = None


class PhotosSaveWallPhotoParams(BaseModel):
    user_id: int = None
    group_id: int = None
    photo: str = None
    server: int = None
    hash: str = None
    latitude: str = None
    longitude: str = None
    caption: str = None


class PhotosGetParams(BaseModel):
    owner_id: str = None
    album_id: str = None
    photo_ids: str = None
    rev: bool = None
    extended: bool = None
    feed_type: str = None
    feed: int = None
    photo_sizes: bool = None
    offset: int = None
    count: int = None


class PhotosGetMarketAlbumUploadServerParams(BaseModel):
    group_id: int = None


class PhotosDeleteCommentParams(BaseModel):
    owner_id: str = None
    comment_id: str = None


class PhotosGetUserPhotosParams(BaseModel):
    user_id: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    sort: str = None


class PhotosGetAllParams(BaseModel):
    owner_id: int = None
    extended: bool = None
    offset: int = None
    count: int = None
    photo_sizes: bool = None
    no_service_albums: bool = None
    need_hidden: bool = None
    skip_hidden: bool = None


class PhotosConfirmTagParams(BaseModel):
    owner_id: int = None
    photo_id: str = None
    tag_id: int = None


class PhotosCopyParams(BaseModel):
    owner_id: int = None
    photo_id: int = None
    access_key: str = None


class PhotosCreateAlbumParams(BaseModel):
    title: str = None
    group_id: int = None
    description: str = None
    privacy: int = None
    comment_privacy: int = None
    privacy_view: str = None
    privacy_comment: str = None
    upload_by_admins_only: bool = None
    comments_disabled: bool = None


class PhotosDeleteParams(BaseModel):
    owner_id: int = None
    photo_id: int = None
    photos: str = None


class PhotosDeleteAlbumParams(BaseModel):
    album_id: int = None
    group_id: int = None


class PhotosEditParams(BaseModel):
    owner_id: str = None
    photo_id: int = None
    caption: str = None
    latitude: str = None
    longitude: str = None
    place_str: str = None
    foursquare_id: str = None
    delete_place: bool = None


class PhotosEditAlbumParams(BaseModel):
    album_id: str = None
    title: str = None
    description: str = None
    owner_id: str = None
    privacy: int = None
    comment_privacy: int = None
    privacy_view: str = None
    privacy_comment: str = None
    upload_by_admins_only: bool = None
    comments_disabled: bool = None


class PhotosGetAlbumsParams(BaseModel):
    owner_id: str = None
    album_ids: str = None
    offset: int = None
    count: int = None
    need_system: bool = None
    need_covers: bool = None
    photo_sizes: bool = None


class PhotosGetByIdParams(BaseModel):
    photos: str = None
    extended: bool = None
    photo_sizes: bool = None


class PhotosGetMessagesUploadServerParams(BaseModel):
    peer_id: int = None


class PhotosGetOwnerPhotoUploadServerParams(BaseModel):
    owner_id: int = None


class PhotosGetTagsParams(BaseModel):
    owner_id: int = None
    photo_id: int = None
    access_key: str = None


class PhotosGetUploadServerParams(BaseModel):
    album_id: int = None
    group_id: int = None


class PhotosMakeCoverParams(BaseModel):
    owner_id: str = None
    photo_id: str = None
    album_id: str = None


class PhotosMoveParams(BaseModel):
    owner_id: str = None
    target_album_id: int = None
    photo_id: str = None


class PhotosRemoveTagParams(BaseModel):
    owner_id: int = None
    photo_id: str = None
    tag_id: int = None


class PhotosSaveParams(BaseModel):
    album_id: int = None
    group_id: int = None
    server: int = None
    photos_list: str = None
    hash: str = None
    latitude: str = None
    longitude: str = None
    caption: str = None


class PhotosSaveOwnerPhotoParams(BaseModel):
    server: str = None
    hash: str = None
    photo: str = None


class PhotosReorderAlbumsParams(BaseModel):
    owner_id: int = None
    album_id: int = None
    before: int = None
    after: int = None


class PhotosSaveMessagesPhotoParams(BaseModel):
    photo: str = None
    server: int = None
    hash: str = None


