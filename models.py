from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True
    )

    password_hash = Column(
        String
    )

class Trade(Base):

    __tablename__ = "trades"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    symbol = Column(String)

    side = Column(String)

    volume = Column(Float)

    profit = Column(Float)

    created_at = Column(DateTime)
