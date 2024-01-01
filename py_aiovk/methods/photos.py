from py_aiovk.types.params.photos import *


class Photos:
    def __init__(self, vk):
        self.vk = vk

    async def get_chat_upload_server(self, params: PhotosGetChatUploadServerParams):
        return await self.vk.execute('photos', 'getChatUploadServer', **params.model_dump(exclude_none=True))

    async def get_owner_cover_photo_upload_server(self, params: PhotosGetOwnerCoverPhotoUploadServerParams):
        return await self.vk.execute('photos', 'getOwnerCoverPhotoUploadServer', **params.model_dump(exclude_none=True))

    async def get_wall_upload_server(self, params: PhotosGetWallUploadServerParams):
        return await self.vk.execute('photos', 'getWallUploadServer', **params.model_dump(exclude_none=True))

    async def save_market_album_photo(self, params: PhotosSaveMarketAlbumPhotoParams):
        return await self.vk.execute('photos', 'saveMarketAlbumPhoto', **params.model_dump(exclude_none=True))

    async def save_owner_cover_photo(self, params: PhotosSaveOwnerCoverPhotoParams):
        return await self.vk.execute('photos', 'saveOwnerCoverPhoto', **params.model_dump(exclude_none=True))

    async def save_wall_photo(self, params: PhotosSaveWallPhotoParams):
        return await self.vk.execute('photos', 'saveWallPhoto', **params.model_dump(exclude_none=True))

    async def get(self, params: PhotosGetParams):
        return await self.vk.execute('photos', 'get', **params.model_dump(exclude_none=True))

    async def get_market_album_upload_server(self, params: PhotosGetMarketAlbumUploadServerParams):
        return await self.vk.execute('photos', 'getMarketAlbumUploadServer', **params.model_dump(exclude_none=True))

    async def delete_comment(self, params: PhotosDeleteCommentParams):
        return await self.vk.execute('photos', 'deleteComment', **params.model_dump(exclude_none=True))

    async def get_user_photos(self, params: PhotosGetUserPhotosParams):
        return await self.vk.execute('photos', 'getUserPhotos', **params.model_dump(exclude_none=True))

    async def get_all(self, params: PhotosGetAllParams):
        return await self.vk.execute('photos', 'getAll', **params.model_dump(exclude_none=True))

    async def confirm_tag(self, params: PhotosConfirmTagParams):
        return await self.vk.execute('photos', 'confirmTag', **params.model_dump(exclude_none=True))

    async def copy(self, params: PhotosCopyParams):
        return await self.vk.execute('photos', 'copy', **params.model_dump(exclude_none=True))

    async def create_album(self, params: PhotosCreateAlbumParams):
        return await self.vk.execute('photos', 'createAlbum', **params.model_dump(exclude_none=True))

    async def delete(self, params: PhotosDeleteParams):
        return await self.vk.execute('photos', 'delete', **params.model_dump(exclude_none=True))

    async def delete_album(self, params: PhotosDeleteAlbumParams):
        return await self.vk.execute('photos', 'deleteAlbum', **params.model_dump(exclude_none=True))

    async def edit(self, params: PhotosEditParams):
        return await self.vk.execute('photos', 'edit', **params.model_dump(exclude_none=True))

    async def edit_album(self, params: PhotosEditAlbumParams):
        return await self.vk.execute('photos', 'editAlbum', **params.model_dump(exclude_none=True))

    async def get_albums(self, params: PhotosGetAlbumsParams):
        return await self.vk.execute('photos', 'getAlbums', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: PhotosGetByIdParams):
        return await self.vk.execute('photos', 'getById', **params.model_dump(exclude_none=True))

    async def get_messages_upload_server(self, params: PhotosGetMessagesUploadServerParams):
        return await self.vk.execute('photos', 'getMessagesUploadServer', **params.model_dump(exclude_none=True))

    async def get_owner_photo_upload_server(self, params: PhotosGetOwnerPhotoUploadServerParams):
        return await self.vk.execute('photos', 'getOwnerPhotoUploadServer', **params.model_dump(exclude_none=True))

    async def get_tags(self, params: PhotosGetTagsParams):
        return await self.vk.execute('photos', 'getTags', **params.model_dump(exclude_none=True))

    async def get_upload_server(self, params: PhotosGetUploadServerParams):
        return await self.vk.execute('photos', 'getUploadServer', **params.model_dump(exclude_none=True))

    async def make_cover(self, params: PhotosMakeCoverParams):
        return await self.vk.execute('photos', 'makeCover', **params.model_dump(exclude_none=True))

    async def move(self, params: PhotosMoveParams):
        return await self.vk.execute('photos', 'move', **params.model_dump(exclude_none=True))

    async def remove_tag(self, params: PhotosRemoveTagParams):
        return await self.vk.execute('photos', 'removeTag', **params.model_dump(exclude_none=True))

    async def save(self, params: PhotosSaveParams):
        return await self.vk.execute('photos', 'save', **params.model_dump(exclude_none=True))

    async def save_owner_photo(self, params: PhotosSaveOwnerPhotoParams):
        return await self.vk.execute('photos', 'saveOwnerPhoto', **params.model_dump(exclude_none=True))

    async def reorder_albums(self, params: PhotosReorderAlbumsParams):
        return await self.vk.execute('photos', 'reorderAlbums', **params.model_dump(exclude_none=True))

    async def save_messages_photo(self, params: PhotosSaveMessagesPhotoParams):
        return await self.vk.execute('photos', 'saveMessagesPhoto', **params.model_dump(exclude_none=True))
