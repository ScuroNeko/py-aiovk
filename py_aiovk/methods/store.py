from py_aiovk.types.params.store import *


class Store:
    def __init__(self, vk):
        self.vk = vk

    async def add_stickers_to_favorite(self, params: StoreAddStickersToFavoriteParams):
        return await self.vk.execute('store', 'addStickersToFavorite', **params.model_dump(exclude_none=True))

    async def get_stickers_keywords(self, params: StoreGetStickersKeywordsParams):
        return await self.vk.execute('store', 'getStickersKeywords', **params.model_dump(exclude_none=True))

    async def remove_stickers_from_favorite(self, params: StoreRemoveStickersFromFavoriteParams):
        return await self.vk.execute('store', 'removeStickersFromFavorite', **params.model_dump(exclude_none=True))

    async def get_products(self, params: StoreGetProductsParams):
        return await self.vk.execute('store', 'getProducts', **params.model_dump(exclude_none=True))

