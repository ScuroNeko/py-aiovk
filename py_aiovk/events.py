from pydantic import BaseModel


class Events:
    MESSAGE_NEW = 'message_new'
    MESSAGE_TYPING_STATE = 'message_typing_state'


class TypingEvent(BaseModel):
    state: str
    from_id: int
    to_id: int
