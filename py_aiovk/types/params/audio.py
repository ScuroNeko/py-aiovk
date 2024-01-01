from pydantic import BaseModel


class AudioAddParams(BaseModel):
    audio_id: int = None
    owner_id: int = None
    group_id: int = None
    playlist_id: int = None
    ref: str = None
    access_key: str = None
    track_code: str = None


class AudioGetUploadServerParams(BaseModel):


class AudioSaveParams(BaseModel):
    server: int = None
    audio: str = None
    hash: str = None
    artist: str = None
    title: str = None


class AudioEditParams(BaseModel):
    owner_id: str = None
    audio_id: str = None
    artist: str = None
    title: str = None
    text: str = None
    genre_id: str = None
    no_search: bool = None


class AudioMoveToAlbumParams(BaseModel):
    group_id: str = None
    album_id: int = None
    audio_ids: str = None


class AudioGetFavoritesParams(BaseModel):
    owner_id: int = None
    offset: int = None
    count: int = None


class AudioAddToFavoritesParams(BaseModel):
    owner_id: int = None
    audio_id: int = None


class AudioDeleteFromFavoritesParams(BaseModel):
    audio_ids: str = None


class AudioSetForDownloadParams(BaseModel):
    owner_id: int = None
    audio_id: int = None


class AudioSetPlaylistForDownloadParams(BaseModel):
    owner_id: int = None
    playlist_id: int = None
    access_key: str = None


