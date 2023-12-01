from pydantic import BaseModel


class NotesGetByIdParams(BaseModel):
    note_id: int = None
    owner_id: int = None
    need_wiki: bool = None


