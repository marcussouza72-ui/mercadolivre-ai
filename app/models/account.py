from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database.connection import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    nickname = Column(String(80), nullable=False)

    meli_user_id = Column(String(50), unique=True)

    access_token = Column(String)

    refresh_token = Column(String)

    token_expires = Column(DateTime)

    active = Column(Boolean, default=True)