from pydantic import BaseModel


class UtilsResolveScreenNameParams(BaseModel):
    screen_name: str = None


