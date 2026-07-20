from fastapi import FastAPI

from mt5_connector import MT5Connector

from routes.auth import router as auth_router
from routes.trades import router as trades_router
from routes.bots import router as bots_router
from websocket import router as ws_router

app = FastAPI(
    title="AI Forex Trader Pro",
    version="1.0.0"
)

mt5 = MT5Connector()

app.include_router(auth_router)
app.include_router(trades_router)
app.include_router(bots_router)
app.include_router(ws_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "system": "AI Forex Trader Pro"
    }


@app.get("/account")
def account():

    mt5.connect()

    info = mt5.account_info()

    return {
        "login": info.login,
        "balance": info.balance,
        "equity": info.equity
    }


@app.get("/price/{symbol}")
def price(symbol: str):

    mt5.connect()

    return mt5.symbol_price(symbol)
