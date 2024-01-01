from enum import Enum
from typing import Type


class VkObject:
    __slots__ = (
        'raw',
    )

    def __init__(self, raw):
        self.raw = raw


class PhotoSize:
    __slots__ = (
        'type', 'url', 'width', 'height'
    )

    def __init__(self, raw: dict):
        self.type: str = raw['type']
        self.url: str = raw['url']
        self.width: int = raw['width']
        self.height: int = raw['height']


class StickerSize:
    __slots__ = (
        'url', 'width', 'height'
    )

    def __init__(self, raw: dict):
        self.url: str = raw['url']
        self.width: int = raw['width']
        self.height: int = raw['height']


class Photo(VkObject):
    __slots__ = (
        'id', 'album_id', 'owner_id', 'access_key',
        'user_id', 'text', 'date', 'sizes',
        'type'
    )

    def __init__(self, raw: dict):
        super().__init__(raw)
        self.type = 'photo'
        self.raw: dict = raw['photo']

        self.id: int = self.raw['id']
        self.album_id: int = self.raw['album_id']
        self.owner_id: int = self.raw['owner_id']
        self.access_key: str = self.raw.get('access_key', '')
        self.user_id: int = self.raw.get('user_id', 0)

        self.text: str = self.raw['text']
        self.date: int = self.raw['date']  # unix time
        self.sizes = [PhotoSize(r) for r in self.raw['sizes']]

    def __repr__(self):
        return f'photo{self.owner_id}_{self.id}'


class Sticker(VkObject):
    __slots__ = (
        'type', 'images', 'images_with_background',
        'animation_url', 'is_allowed'
    )

    def __init__(self, raw: dict):
        super().__init__(raw)

        self.type = 'sticker'
        self.raw: dict = raw['sticker']

        self.images = [StickerSize(img) for img in self.raw['images']]
        self.images_with_background = [StickerSize(img) for img in self.raw['images_with_background']]

        self.animation_url = self.raw.get('animation_url', '')
        self.is_allowed = self.raw.get('is_allowed')

    def __repr__(self):
        return f'sticker{self}'


class DocumentType(Enum):
    TEXT = 1
    ARCHIVE = 2
    GIF = 3
    PHOTO = 4
    AUDIO = 5
    VIDEO = 6
    BOOKS = 7
    UNKNOWN = 8


class Document(VkObject):
    __slots__ = (
        'id', 'album_id', 'owner_id',
        'title', 'size', 'ext', 'url',
        'date', 'type'
    )

    def __init__(self, raw: dict):
        super().__init__(raw)
        self.raw: dict = raw['doc']
        self.id: int = self.raw['id']
        self.owner_id: int = self.raw['owner_id']

        self.title: str = self.raw['title']
        self.size: int = self.raw['size']  # размер в байтах
        self.ext: str = self.raw['ext']  # расширение
        self.url: str = self.raw['url']
        self.date: int = self.raw['date']  # unix time
        self.type: DocumentType = self.raw['type']

    def __repr__(self):
        return f'doc{self.owner_id}_{self.id}'


Attachment = Type[Photo], Type[Document], Type[Sticker]


def load_attachments(raw: list[dict]) -> list[Attachment]:
    attachments = []
    for attachment in raw:
        match attachment['type']:
            case 'photo':
                attachments.append(Photo(attachment))
            case 'doc':
                attachments.append(Document(attachment))
            case 'sticker':
                attachments.append(Sticker(attachment))
            case _:
                attachments.append(VkObject(attachment))
    return attachments


def dump_attachments(raw_attachments: list[Attachment]) -> str:
    return ','.join(map(repr, raw_attachments))
