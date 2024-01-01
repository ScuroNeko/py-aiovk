from pydantic import BaseModel


class BoardDeleteCommentParams(BaseModel):
    group_id: str = None
    topic_id: str = None
    comment_id: str = None


class BoardDeleteTopicParams(BaseModel):
    group_id: int = None
    topic_id: int = None


class BoardGetCommentsParams(BaseModel):
    group_id: int = None
    topic_id: int = None
    need_likes: bool = None
    start_comment_id: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    sort: str = None


class BoardGetTopicsParams(BaseModel):
    group_id: int = None
    topic_ids: str = None
    order: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    preview: int = None
    preview_length: int = None


class BoardEditCommentParams(BaseModel):
    group_id: str = None
    topic_id: str = None
    comment_id: str = None
    message: str = None
    attachments: str = None


