from pydantic import BaseModel


class Photo(BaseModel):
    owner_id: int