from py_aiovk.types.params.messages import *


class Messages:
    def __init__(self, vk):
        self.vk = vk

    async def send(self, params: MessagesSendParams):
        return await self.vk.execute('messages', 'send', **params.model_dump(exclude_none=True))

    async def join_chat_by_invite_link(self, params: MessagesJoinChatByInviteLinkParams):
        return await self.vk.execute('messages', 'joinChatByInviteLink', **params.model_dump(exclude_none=True))

    async def get_chat_preview(self, params: MessagesGetChatPreviewParams):
        return await self.vk.execute('messages', 'getChatPreview', **params.model_dump(exclude_none=True))

    async def set_chat_photo(self, params: MessagesSetChatPhotoParams):
        return await self.vk.execute('messages', 'setChatPhoto', **params.model_dump(exclude_none=True))

    async def add_chat_user(self, params: MessagesAddChatUserParams):
        return await self.vk.execute('messages', 'addChatUser', **params.model_dump(exclude_none=True))

    async def edit_chat(self, params: MessagesEditChatParams):
        return await self.vk.execute('messages', 'editChat', **params.model_dump(exclude_none=True))

    async def unpin(self, params: MessagesUnpinParams):
        return await self.vk.execute('messages', 'unpin', **params.model_dump(exclude_none=True))

    async def pin(self, params: MessagesPinParams):
        return await self.vk.execute('messages', 'pin', **params.model_dump(exclude_none=True))

    async def remove_chat_user(self, params: MessagesRemoveChatUserParams):
        return await self.vk.execute('messages', 'removeChatUser', **params.model_dump(exclude_none=True))

    async def create_chat(self, params: MessagesCreateChatParams):
        return await self.vk.execute('messages', 'createChat', **params.model_dump(exclude_none=True))

    async def set_activity(self, params: MessagesSetActivityParams):
        return await self.vk.execute('messages', 'setActivity', **params.model_dump(exclude_none=True))

    async def allow_messages_from_group(self, params: MessagesAllowMessagesFromGroupParams):
        return await self.vk.execute('messages', 'allowMessagesFromGroup', **params.model_dump(exclude_none=True))

    async def deny_messages_from_group(self, params: MessagesDenyMessagesFromGroupParams):
        return await self.vk.execute('messages', 'denyMessagesFromGroup', **params.model_dump(exclude_none=True))

    async def get_invite_link(self, params: MessagesGetInviteLinkParams):
        return await self.vk.execute('messages', 'getInviteLink', **params.model_dump(exclude_none=True))

    async def mark_as_read(self, params: MessagesMarkAsReadParams):
        return await self.vk.execute('messages', 'markAsRead', **params.model_dump(exclude_none=True))

    async def edit(self, params: MessagesEditParams):
        return await self.vk.execute('messages', 'edit', **params.model_dump(exclude_none=True))

    async def delete_chat_photo(self, params: MessagesDeleteChatPhotoParams):
        return await self.vk.execute('messages', 'deleteChatPhoto', **params.model_dump(exclude_none=True))

    async def delete_conversation(self, params: MessagesDeleteConversationParams):
        return await self.vk.execute('messages', 'deleteConversation', **params.model_dump(exclude_none=True))

    async def search_conversations(self, params: MessagesSearchConversationsParams):
        return await self.vk.execute('messages', 'searchConversations', **params.model_dump(exclude_none=True))

    async def search(self, params: MessagesSearchParams):
        return await self.vk.execute('messages', 'search', **params.model_dump(exclude_none=True))

    async def get_by_conversation_message_id(self, params: MessagesGetByConversationMessageIdParams):
        return await self.vk.execute('messages', 'getByConversationMessageId', **params.model_dump(exclude_none=True))

    async def get_by_id(self, params: MessagesGetByIdParams):
        return await self.vk.execute('messages', 'getById', **params.model_dump(exclude_none=True))

    async def get_conversation_members(self, params: MessagesGetConversationMembersParams):
        return await self.vk.execute('messages', 'getConversationMembers', **params.model_dump(exclude_none=True))

    async def get_conversations_by_id(self, params: MessagesGetConversationsByIdParams):
        return await self.vk.execute('messages', 'getConversationsById', **params.model_dump(exclude_none=True))

    async def get_history(self, params: MessagesGetHistoryParams):
        return await self.vk.execute('messages', 'getHistory', **params.model_dump(exclude_none=True))

    async def get_history_attachments(self, params: MessagesGetHistoryAttachmentsParams):
        return await self.vk.execute('messages', 'getHistoryAttachments', **params.model_dump(exclude_none=True))

    async def get_join_link(self, params: MessagesGetJoinLinkParams):
        return await self.vk.execute('messages', 'getJoinLink', **params.model_dump(exclude_none=True))

    async def start_call(self, params: MessagesStartCallParams):
        return await self.vk.execute('messages', 'startCall', **params.model_dump(exclude_none=True))

    async def delete(self, params: MessagesDeleteParams):
        return await self.vk.execute('messages', 'delete', **params.model_dump(exclude_none=True))

    async def is_messages_from_group_allowed(self, params: MessagesIsMessagesFromGroupAllowedParams):
        return await self.vk.execute('messages', 'isMessagesFromGroupAllowed', **params.model_dump(exclude_none=True))

    async def get_long_poll_server(self, params: MessagesGetLongPollServerParams):
        return await self.vk.execute('messages', 'getLongPollServer', **params.model_dump(exclude_none=True))

    async def get_recent_graffities(self, params: MessagesGetRecentGraffitiesParams):
        return await self.vk.execute('messages', 'getRecentGraffities', **params.model_dump(exclude_none=True))

    async def hide_recent_graffiti(self, params: MessagesHideRecentGraffitiParams):
        return await self.vk.execute('messages', 'hideRecentGraffiti', **params.model_dump(exclude_none=True))

    async def force_call_finish(self, params: MessagesForceCallFinishParams):
        return await self.vk.execute('messages', 'forceCallFinish', **params.model_dump(exclude_none=True))

    async def get_conversations(self, params: MessagesGetConversationsParams):
        return await self.vk.execute('messages', 'getConversations', **params.model_dump(exclude_none=True))

