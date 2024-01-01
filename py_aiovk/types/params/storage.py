from pydantic import BaseModel


class StorageGetParams(BaseModel):
    key: str = None
    keys: str = None
    user_id: int = None


class StorageGetKeysParams(BaseModel):
    user_id: int = None
    offset: int = None
    count: int = None


class StorageSetParams(BaseModel):
    key: str = None
    value: str = None
    user_id: int = None


