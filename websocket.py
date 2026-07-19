from fastapi import APIRouter
from fastapi import WebSocket

router = APIRouter()

connections = []

@router.websocket("/ws")

async def websocket_endpoint(
    websocket: WebSocket
):

    await websocket.accept()

    connections.append(websocket)

    while True:

        await websocket.send_json({
            "status": "connected"
        })
