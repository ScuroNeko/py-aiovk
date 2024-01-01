from py_aiovk.types.params.video import *


class Video:
    def __init__(self, vk):
        self.vk = vk

    async def get(self, params: VideoGetParams):
        return await self.vk.execute('video', 'get', **params.model_dump(exclude_none=True))

    async def stop_streaming(self, params: VideoStopStreamingParams):
        return await self.vk.execute('video', 'stopStreaming', **params.model_dump(exclude_none=True))

    async def get_albums(self, params: VideoGetAlbumsParams):
        return await self.vk.execute('video', 'getAlbums', **params.model_dump(exclude_none=True))

    async def get_live_status(self, params: VideoGetLiveStatusParams):
        return await self.vk.execute('video', 'getLiveStatus', **params.model_dump(exclude_none=True))

    async def create_comment(self, params: VideoCreateCommentParams):
        return await self.vk.execute('video', 'createComment', **params.model_dump(exclude_none=True))

    async def edit(self, params: VideoEditParams):
        return await self.vk.execute('video', 'edit', **params.model_dump(exclude_none=True))

    async def add(self, params: VideoAddParams):
        return await self.vk.execute('video', 'add', **params.model_dump(exclude_none=True))

    async def add_album(self, params: VideoAddAlbumParams):
        return await self.vk.execute('video', 'addAlbum', **params.model_dump(exclude_none=True))

    async def delete(self, params: VideoDeleteParams):
        return await self.vk.execute('video', 'delete', **params.model_dump(exclude_none=True))

    async def delete_album(self, params: VideoDeleteAlbumParams):
        return await self.vk.execute('video', 'deleteAlbum', **params.model_dump(exclude_none=True))

    async def delete_comment(self, params: VideoDeleteCommentParams):
        return await self.vk.execute('video', 'deleteComment', **params.model_dump(exclude_none=True))

    async def edit_album(self, params: VideoEditAlbumParams):
        return await self.vk.execute('video', 'editAlbum', **params.model_dump(exclude_none=True))

    async def get_album_by_id(self, params: VideoGetAlbumByIdParams):
        return await self.vk.execute('video', 'getAlbumById', **params.model_dump(exclude_none=True))

    async def get_comments(self, params: VideoGetCommentsParams):
        return await self.vk.execute('video', 'getComments', **params.model_dump(exclude_none=True))

    async def get_long_poll_server(self, params: VideoGetLongPollServerParams):
        return await self.vk.execute('video', 'getLongPollServer', **params.model_dump(exclude_none=True))

    async def live_add_ban(self, params: VideoLiveAddBanParams):
        return await self.vk.execute('video', 'liveAddBan', **params.model_dump(exclude_none=True))

    async def live_delete_ban(self, params: VideoLiveDeleteBanParams):
        return await self.vk.execute('video', 'liveDeleteBan', **params.model_dump(exclude_none=True))

    async def live_send_gift(self, params: VideoLiveSendGiftParams):
        return await self.vk.execute('video', 'liveSendGift', **params.model_dump(exclude_none=True))

    async def remove_from_album(self, params: VideoRemoveFromAlbumParams):
        return await self.vk.execute('video', 'removeFromAlbum', **params.model_dump(exclude_none=True))

    async def save(self, params: VideoSaveParams):
        return await self.vk.execute('video', 'save', **params.model_dump(exclude_none=True))

    async def start_streaming(self, params: VideoStartStreamingParams):
        return await self.vk.execute('video', 'startStreaming', **params.model_dump(exclude_none=True))

