from pydantic import BaseModel


class FaveGetPhotosParams(BaseModel):
    offset: int = None
    count: int = None


class FaveAddArticleParams(BaseModel):
    url: str = None


class FaveAddProductParams(BaseModel):
    owner_id: int = None
    id: int = None
    access_key: str = None


class FaveAddPageParams(BaseModel):
    user_id: int = None
    group_id: int = None


class FaveAddPostParams(BaseModel):
    owner_id: int = None
    id: int = None
    access_key: str = None
    ref: str = None
    track_code: str = None
    source: str = None


class FaveAddTagParams(BaseModel):
    name: str = None
    position: str = None


class FaveAddVideoParams(BaseModel):
    owner_id: int = None
    id: int = None
    access_key: str = None


class FaveEditTagParams(BaseModel):
    id: int = None
    name: str = None


class FaveAddLinkParams(BaseModel):
    link: str = None


class FaveRemoveLinkParams(BaseModel):
    link_id: str = None


class FaveRemoveArticleParams(BaseModel):
    owner_id: int = None
    article_id: int = None
    ref: str = None


class FaveRemoveProductParams(BaseModel):
    owner_id: int = None
    id: int = None


class FaveRemovePageParams(BaseModel):
    user_id: int = None
    group_id: int = None


class FaveRemovePostParams(BaseModel):
    owner_id: int = None
    id: int = None


class FaveRemoveTagParams(BaseModel):
    id: int = None


class FaveRemoveVideoParams(BaseModel):
    owner_id: int = None
    id: int = None


class FaveReorderTagsParams(BaseModel):
    ids: str = None


class FaveSetPageTagsParams(BaseModel):
    user_id: int = None
    group_id: int = None
    tag_ids: str = None


class FaveSetTagsParams(BaseModel):
    item_type: str = None
    item_owner_id: int = None
    item_id: int = None
    tag_ids: str = None
    link_id: str = None
    link_url: str = None


class FaveTrackPageInteractionParams(BaseModel):
    user_id: int = None
    group_id: int = None


class FaveGetPagesParams(BaseModel):
    offset: int = None
    count: int = None
    type: str = None
    fields: str = None
    tag_id: int = None


