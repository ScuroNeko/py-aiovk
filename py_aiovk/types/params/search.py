from pydantic import BaseModel


class SearchGetHintsParams(BaseModel):
    q: str = None
    offset: int = None
    limit: int = None
    filters: str = None
    fields: str = None
    search_global: bool = None


