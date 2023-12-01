from pydantic import BaseModel


class MessagesSendParams(BaseModel):
    user_id: int = None
    random_id: int = None
    peer_id: int = None
    peer_ids: str = None
    domain: str = None
    chat_id: int = None
    user_ids: str = None
    message: str = None
    guid: int = None
    lat: str = None
    long: str = None
    attachment: str = None
    reply_to: int = None
    forward_messages: str = None
    forward: str = None
    sticker_id: int = None
    group_id: int = None
    keyboard: str = None
    template: str = None
    payload: str = None
    content_source: str = None
    dont_parse_links: bool = None
    disable_mentions: bool = None
    intent: str = None
    subscribe_id: int = None


class MessagesJoinChatByInviteLinkParams(BaseModel):
    link: str = None


class MessagesGetChatPreviewParams(BaseModel):
    peer_id: int = None
    link: str = None
    fields: str = None


class MessagesSetChatPhotoParams(BaseModel):
    file: str = None


class MessagesAddChatUserParams(BaseModel):
    chat_id: int = None
    user_id: int = None
    visible_messages_count: int = None


class MessagesEditChatParams(BaseModel):
    chat_id: int = None
    title: str = None


class MessagesUnpinParams(BaseModel):
    peer_id: int = None
    group_id: int = None


class MessagesPinParams(BaseModel):
    peer_id: int = None
    message_id: int = None
    conversation_message_id: int = None


class MessagesRemoveChatUserParams(BaseModel):
    chat_id: int = None
    user_id: int = None
    member_id: int = None


class MessagesCreateChatParams(BaseModel):
    user_ids: str = None
    title: str = None
    group_id: int = None


class MessagesSetActivityParams(BaseModel):
    user_id: str = None
    type: str = None
    peer_id: int = None
    group_id: int = None


class MessagesAllowMessagesFromGroupParams(BaseModel):
    group_id: int = None
    key: str = None


class MessagesDenyMessagesFromGroupParams(BaseModel):
    group_id: int = None


class MessagesGetInviteLinkParams(BaseModel):
    peer_id: int = None
    reset: bool = None
    group_id: int = None


class MessagesMarkAsReadParams(BaseModel):
    message_ids: str = None
    peer_id: str = None
    start_message_id: int = None
    group_id: int = None
    mark_conversation_as_read: bool = None
    up_to_cmid: int = None


class MessagesEditParams(BaseModel):
    peer_id: int = None
    message: str = None
    lat: str = None
    long: str = None
    attachment: str = None
    keep_forward_messages: bool = None
    keep_snippets: bool = None
    group_id: int = None
    dont_parse_links: bool = None
    disable_mentions: bool = None
    message_id: int = None
    conversation_message_id: int = None
    template: str = None
    keyboard: str = None


class MessagesDeleteChatPhotoParams(BaseModel):
    chat_id: int = None
    group_id: int = None


class MessagesDeleteConversationParams(BaseModel):
    user_id: int = None
    peer_id: int = None
    offset: int = None
    count: int = None
    group_id: int = None


class MessagesSearchConversationsParams(BaseModel):
    q: str = None
    count: int = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesSearchParams(BaseModel):
    q: str = None
    peer_id: int = None
    date: int = None
    preview_length: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesGetByConversationMessageIdParams(BaseModel):
    peer_id: int = None
    conversation_message_ids: str = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesGetByIdParams(BaseModel):
    message_ids: str = None
    preview_length: int = None
    extended: bool = None
    fields: str = None
    group_id: int = None
    cmids: str = None
    peer_id: int = None


class MessagesGetConversationMembersParams(BaseModel):
    peer_id: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesGetConversationsByIdParams(BaseModel):
    peer_ids: str = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesGetHistoryParams(BaseModel):
    offset: int = None
    count: int = None
    user_id: str = None
    peer_id: int = None
    start_message_id: int = None
    rev: int = None
    extended: bool = None
    fields: str = None
    group_id: int = None


class MessagesGetHistoryAttachmentsParams(BaseModel):
    attachment_types: str = None
    group_id: int = None
    peer_id: int = None
    cmid: int = None
    attachment_position: int = None
    offset: int = None
    count: int = None
    extended: bool = None
    fields: str = None
    max_forwards_level: int = None
    message_video: bool = None
    media_type: str = None
    start_from: str = None
    preserve_order: bool = None
    photo_sizes: bool = None


class MessagesGetJoinLinkParams(BaseModel):
    call_id: str = None
    invalidate: bool = None


class MessagesStartCallParams(BaseModel):
    group_id: int = None


class MessagesDeleteParams(BaseModel):
    message_ids: str = None
    spam: bool = None
    reason: int = None
    group_id: int = None
    delete_for_all: bool = None
    peer_id: int = None
    cmids: str = None


class MessagesIsMessagesFromGroupAllowedParams(BaseModel):
    group_id: int = None
    user_id: int = None


class MessagesGetLongPollServerParams(BaseModel):
    need_pts: bool = None
    group_id: int = None
    lp_version: int = None


class MessagesGetRecentGraffitiesParams(BaseModel):
    limit: int = None


class MessagesHideRecentGraffitiParams(BaseModel):
    doc_id: int = None


class MessagesForceCallFinishParams(BaseModel):
    call_id: str = None


class MessagesGetConversationsParams(BaseModel):
    offset: int = None
    count: int = None
    filter: str = None
    extended: bool = None
    start_message_id: int = None
    fields: str = None
    group_id: int = None


