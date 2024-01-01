from pydantic import BaseModel


class StoreAddStickersToFavoriteParams(BaseModel):
    sticker_ids: str = None


class StoreGetStickersKeywordsParams(BaseModel):
    stickers_ids: str = None
    products_ids: str = None
    aliases: bool = None
    all_products: bool = None
    need_stickers: bool = None


class StoreRemoveStickersFromFavoriteParams(BaseModel):
    sticker_ids: str = None


class StoreGetProductsParams(BaseModel):
    type: str = None
    merchant: str = None
    section: str = None
    product_ids: str = None
    filters: str = None
    extended: bool = None


