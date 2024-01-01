from pydantic import BaseModel


class DonutGetSubscriptionsParams(BaseModel):
    fields: str = None
    offset: int = None
    count: int = None


class DonutGetFriendsParams(BaseModel):
    owner_id: int = None
    offset: int = None
    count: int = None
    fields: str = None


