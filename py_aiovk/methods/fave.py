from py_aiovk.types.params.fave import *


class Fave:
    def __init__(self, vk):
        self.vk = vk

    async def get_photos(self, params: FaveGetPhotosParams):
        return await self.vk.execute('fave', 'getPhotos', **params.model_dump(exclude_none=True))

    async def add_article(self, params: FaveAddArticleParams):
        return await self.vk.execute('fave', 'addArticle', **params.model_dump(exclude_none=True))

    async def add_product(self, params: FaveAddProductParams):
        return await self.vk.execute('fave', 'addProduct', **params.model_dump(exclude_none=True))

    async def add_page(self, params: FaveAddPageParams):
        return await self.vk.execute('fave', 'addPage', **params.model_dump(exclude_none=True))

    async def add_post(self, params: FaveAddPostParams):
        return await self.vk.execute('fave', 'addPost', **params.model_dump(exclude_none=True))

    async def add_tag(self, params: FaveAddTagParams):
        return await self.vk.execute('fave', 'addTag', **params.model_dump(exclude_none=True))

    async def add_video(self, params: FaveAddVideoParams):
        return await self.vk.execute('fave', 'addVideo', **params.model_dump(exclude_none=True))

    async def edit_tag(self, params: FaveEditTagParams):
        return await self.vk.execute('fave', 'editTag', **params.model_dump(exclude_none=True))

    async def add_link(self, params: FaveAddLinkParams):
        return await self.vk.execute('fave', 'addLink', **params.model_dump(exclude_none=True))

    async def remove_link(self, params: FaveRemoveLinkParams):
        return await self.vk.execute('fave', 'removeLink', **params.model_dump(exclude_none=True))

    async def remove_article(self, params: FaveRemoveArticleParams):
        return await self.vk.execute('fave', 'removeArticle', **params.model_dump(exclude_none=True))

    async def remove_product(self, params: FaveRemoveProductParams):
        return await self.vk.execute('fave', 'removeProduct', **params.model_dump(exclude_none=True))

    async def remove_page(self, params: FaveRemovePageParams):
        return await self.vk.execute('fave', 'removePage', **params.model_dump(exclude_none=True))

    async def remove_post(self, params: FaveRemovePostParams):
        return await self.vk.execute('fave', 'removePost', **params.model_dump(exclude_none=True))

    async def remove_tag(self, params: FaveRemoveTagParams):
        return await self.vk.execute('fave', 'removeTag', **params.model_dump(exclude_none=True))

    async def remove_video(self, params: FaveRemoveVideoParams):
        return await self.vk.execute('fave', 'removeVideo', **params.model_dump(exclude_none=True))

    async def reorder_tags(self, params: FaveReorderTagsParams):
        return await self.vk.execute('fave', 'reorderTags', **params.model_dump(exclude_none=True))

    async def set_page_tags(self, params: FaveSetPageTagsParams):
        return await self.vk.execute('fave', 'setPageTags', **params.model_dump(exclude_none=True))

    async def set_tags(self, params: FaveSetTagsParams):
        return await self.vk.execute('fave', 'setTags', **params.model_dump(exclude_none=True))

    async def track_page_interaction(self, params: FaveTrackPageInteractionParams):
        return await self.vk.execute('fave', 'trackPageInteraction', **params.model_dump(exclude_none=True))

    async def get_pages(self, params: FaveGetPagesParams):
        return await self.vk.execute('fave', 'getPages', **params.model_dump(exclude_none=True))

