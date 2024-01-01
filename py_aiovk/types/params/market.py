from pydantic import BaseModel


class MarketDeleteAlbumParams(BaseModel):
    owner_id: int = None
    album_id: int = None


class MarketDeleteCommentParams(BaseModel):
    owner_id: int = None
    comment_id: int = None


class MarketEditAlbumParams(BaseModel):
    owner_id: int = None
    album_id: int = None
    title: str = None
    photo_id: int = None
    main_album: bool = None
    is_hidden: bool = None


class MarketGetAlbumByIdParams(BaseModel):
    owner_id: int = None
    album_ids: str = None
    need_all_item_ids: bool = None


class MarketGetCategoriesParams(BaseModel):
    count: int = None
    offset: int = None


class MarketSearchParams(BaseModel):
    owner_id: int = None
    album_id: int = None
    q: str = None
    price_from: int = None
    price_to: int = None
    sort: int = None
    rev: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    status: str = None
    need_variants: bool = None


class MarketSearchItemsParams(BaseModel):
    q: str = None
    offset: int = None
    count: int = None
    category_id: int = None
    price_from: int = None
    price_to: int = None
    sort_by: int = None
    sort_direction: int = None
    country: int = None
    city: int = None


class MarketAddAlbumParams(BaseModel):
    owner_id: int = None
    title: str = None
    photo_id: int = None
    main_album: bool = None
    is_hidden: bool = None


class MarketCreateCommentParams(BaseModel):
    owner_id: int = None
    item_id: int = None
    message: str = None
    attachments: str = None
    from_group: bool = None
    reply_to_comment: int = None
    sticker_id: int = None
    guid: str = None


class MarketDeleteParams(BaseModel):
    owner_id: int = None
    item_id: int = None


class MarketGetParams(BaseModel):
    owner_id: int = None
    album_id: int = None
    count: int = None
    offset: int = None
    extended: bool = None
    date_from: str = None
    date_to: str = None
    need_variants: bool = None
    with_disabled: bool = None


class MarketGetByIdParams(BaseModel):
    item_ids: str = None
    extended: bool = None
    ref_screen: str = None
    ref_post_id: str = None


class MarketGetOrderByIdParams(BaseModel):
    user_id: int = None
    order_id: int = None
    extended: bool = None


class MarketGetOrderItemsParams(BaseModel):
    user_id: int = None
    order_id: int = None
    offset: int = None
    count: int = None


class MarketGetOrdersParams(BaseModel):
    offset: int = None
    count: int = None
    extended: bool = None
    date_from: str = None
    date_to: str = None


class MarketEditCommentParams(BaseModel):
    owner_id: int = None
    comment_id: int = None
    message: str = None
    attachments: str = None


