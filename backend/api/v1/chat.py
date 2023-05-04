import uuid

from fastapi import WebSocket, WebSocketDisconnect, WebSocketException
from starlette import status

from backend.usecase import ChatUsecase
from .wsmanager import manager


class ChatHandler:
    def __init__(self, usecase: ChatUsecase = ChatUsecase()):
        self.usecase = usecase

    async def create_chat(
        self, websocket: WebSocket, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> None:
        try:
            await self.usecase.create_chat(user_id, friend_id)
        except ValueError as e:
            raise WebSocketException(
                code=status.HTTP_403_FORBIDDEN, reason=str(e)
            )

        await manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                await manager.send_personal_message(data, websocket)
        except WebSocketDisconnect:
            manager.disconnect(websocket)
            await manager.broadcast(f"Client #{websocket} left the chat")
