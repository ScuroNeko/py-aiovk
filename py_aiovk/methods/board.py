from py_aiovk.types.params.board import *


class Board:
    def __init__(self, vk):
        self.vk = vk

    async def delete_comment(self, params: BoardDeleteCommentParams):
        return await self.vk.execute('board', 'deleteComment', **params.model_dump(exclude_none=True))

    async def delete_topic(self, params: BoardDeleteTopicParams):
        return await self.vk.execute('board', 'deleteTopic', **params.model_dump(exclude_none=True))

    async def get_comments(self, params: BoardGetCommentsParams):
        return await self.vk.execute('board', 'getComments', **params.model_dump(exclude_none=True))

    async def get_topics(self, params: BoardGetTopicsParams):
        return await self.vk.execute('board', 'getTopics', **params.model_dump(exclude_none=True))

    async def edit_comment(self, params: BoardEditCommentParams):
        return await self.vk.execute('board', 'editComment', **params.model_dump(exclude_none=True))

