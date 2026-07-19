from pydantic import BaseModel

class UserRegister(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TradeRequest(BaseModel):
    symbol: str
    side: str
    volume: float

class BotRequest(BaseModel):
    symbol: str
