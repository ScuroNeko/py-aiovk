from pydantic import BaseModel


class AppWidgetsUpdateParams(BaseModel):
    code: str = None
    type: str = None


