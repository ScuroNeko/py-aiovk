from py_aiovk.types.params.market import *


class Market:
    def __init__(self, vk):
        self.vk = vk

    async def delete_album(self, params: MarketDeleteAlbumParams):
        return await self.vk.execute('market', 'deleteAlbum', **params.model_dump(exclude_none=True))

    async def delete_comment(self, params: MarketDeleteCommentParams):
        return await self.vk.execute('market', 'deleteComment', **params.model_dump(exclude_none=True))

    async def edit_album(self, params: MarketEditAlbumParams):
        return await self.vk.execute('market', 'editAlbum', **params.model_dump(exclude_none=True))

    async def get_album_by_id(self, params: MarketGetAlbumByIdParams):
        return await self.vk.execute('market', 'getAlbumById', **params.model_dump(exclude_none=True))

    async def get_categories(self, params: MarketGetCategoriesParams):
        return await self.vk.execute('market', 'getCategories', **params.model_dump(exclude_none=True))

    async def search(self, params: MarketSearchParams):
        return await self.vk.execute('market', 'search', **params.model_dump(exclude_none=True))

    async def search_items(self, params: MarketSearchItemsParams):
        return await self.vk.execute('market', 'searchItems', **params.model_dump(exclude_none=True))

    async def add_album(self, params: MarketAddAlbumParams):
        return await self.vk.execute('market', 'addAlbum', **params.model_dump(exclude_none=True))

    async def create_comment(self, params: MarketCreateCommentParams):
        return await self.vk.execute('market', 'createComment', **params.model_dump(exclude_none=True))

    async def delete(self, params: MarketDeleteParams):
        return await self.vk.execute('market', 'delete', **params.model_dump(exclude_none=True))

    async def get(self, params: MarketGetParams):
        return await self.vk.execute('market', 'get', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: MarketGetByIdParams):
        return await self.vk.execute('market', 'getById', **params.model_dump(exclude_none=True))

    async def get_order_by_id(self, params: MarketGetOrderByIdParams):
        return await self.vk.execute('market', 'getOrderById', **params.model_dump(exclude_none=True))

    async def get_order_items(self, params: MarketGetOrderItemsParams):
        return await self.vk.execute('market', 'getOrderItems', **params.model_dump(exclude_none=True))

    async def get_orders(self, params: MarketGetOrdersParams):
        return await self.vk.execute('market', 'getOrders', **params.model_dump(exclude_none=True))

    async def edit_comment(self, params: MarketEditCommentParams):
        return await self.vk.execute('market', 'editComment', **params.model_dump(exclude_none=True))

