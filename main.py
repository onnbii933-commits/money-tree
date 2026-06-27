from fastapi import FastAPI

from mt5_connector import MT5Connector

app = FastAPI()

mt5 = MT5Connector()

@app.get("/")
def root():

    return {
        "status": "online"
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
def price(symbol):

    mt5.connect()

    return mt5.symbol_price(
        symbol
    )
