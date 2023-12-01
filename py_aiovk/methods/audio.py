from py_aiovk.types.params.audio import *


class Audio:
    def __init__(self, vk):
        self.vk = vk

    async def add(self, params: AudioAddParams):
        return await self.vk.execute('audio', 'add', **params.model_dump(exclude_none=True))

    async def get_upload_server(self, params: AudioGetUploadServerParams):
        return await self.vk.execute('audio', 'getUploadServer', **params.model_dump(exclude_none=True))

    async def save(self, params: AudioSaveParams):
        return await self.vk.execute('audio', 'save', **params.model_dump(exclude_none=True))

    async def edit(self, params: AudioEditParams):
        return await self.vk.execute('audio', 'edit', **params.model_dump(exclude_none=True))

    async def move_to_album(self, params: AudioMoveToAlbumParams):
        return await self.vk.execute('audio', 'moveToAlbum', **params.model_dump(exclude_none=True))

    async def get_favorites(self, params: AudioGetFavoritesParams):
        return await self.vk.execute('audio', 'getFavorites', **params.model_dump(exclude_none=True))

    async def add_to_favorites(self, params: AudioAddToFavoritesParams):
        return await self.vk.execute('audio', 'addToFavorites', **params.model_dump(exclude_none=True))

    async def delete_from_favorites(self, params: AudioDeleteFromFavoritesParams):
        return await self.vk.execute('audio', 'deleteFromFavorites', **params.model_dump(exclude_none=True))

    async def set_for_download(self, params: AudioSetForDownloadParams):
        return await self.vk.execute('audio', 'setForDownload', **params.model_dump(exclude_none=True))

    async def set_playlist_for_download(self, params: AudioSetPlaylistForDownloadParams):
        return await self.vk.execute('audio', 'setPlaylistForDownload', **params.model_dump(exclude_none=True))
