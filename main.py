from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.trades import router as trades_router
from routes.bots import router as bots_router

from websocket import router as ws_router

app = FastAPI()

app.include_router(auth_router)

app.include_router(trades_router)

app.include_router(bots_router)

app.include_router(ws_router)

@app.get("/")
def root():

    return {
        "status":
        "online"
    }
