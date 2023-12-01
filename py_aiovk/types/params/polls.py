from pydantic import BaseModel


class PollsGetVotersParams(BaseModel):
    owner_id: int = None
    poll_id: int = None
    answer_ids: str = None
    is_board: bool = None
    friends_only: bool = None
    offset: int = None
    count: int = None
    fields: str = None
    name_case: str = None


class PollsGetPhotoUploadServerParams(BaseModel):
    owner_id: int = None


class PollsSavePhotoParams(BaseModel):
    photo: str = None
    hash: str = None


class PollsCreateParams(BaseModel):
    question: str = None
    is_anonymous: bool = None
    is_multiple: bool = None
    end_date: int = None
    owner_id: int = None
    app_id: int = None
    add_answers: str = None
    photo_id: int = None
    background_id: str = None
    disable_unvote: bool = None


class PollsGetByIdParams(BaseModel):
    owner_id: int = None
    is_board: bool = None
    poll_id: int = None
    extended: bool = None
    friends_count: int = None
    fields: str = None
    name_case: str = None


