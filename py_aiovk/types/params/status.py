from pydantic import BaseModel


class StatusSetParams(BaseModel):
    text: str = None
    group_id: int = None


