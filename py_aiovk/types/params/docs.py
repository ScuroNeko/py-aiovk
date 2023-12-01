from pydantic import BaseModel


class DocsGetUploadServerParams(BaseModel):
    group_id: int = None


class DocsAddParams(BaseModel):
    owner_id: int = None
    doc_id: int = None
    access_key: str = None


class DocsDeleteParams(BaseModel):
    owner_id: int = None
    doc_id: int = None


class DocsGetByIdParams(BaseModel):
    docs: str = None
    return_tags: bool = None


class DocsGetParams(BaseModel):
    count: int = None
    offset: int = None
    type: int = None
    owner_id: int = None
    return_tags: bool = None


class DocsSaveParams(BaseModel):
    file: str = None
    title: str = None
    tags: str = None
    return_tags: bool = None


class DocsSearchParams(BaseModel):
    q: str = None
    search_own: bool = None
    count: int = None
    offset: int = None
    return_tags: bool = None


