from pydantic import BaseModel


class AuthCheckPhoneParams(BaseModel):
    phone: str = None
    client_id: int = None
    client_secret: str = None
    auth_by_phone: bool = None


