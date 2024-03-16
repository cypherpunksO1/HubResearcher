from sqlalchemy import Column
from sqlalchemy import (Integer,
                        String,
                        DateTime,
                        UUID)
import asyncio
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base

from src.main.base import Base, engine, init_models
from src.mixins.serializer_mixin import SerializerMixin

from datetime import datetime


class User(Base, SerializerMixin):
    __tablename__ = 'user'

    pk = Column(Integer, primary_key=True)
    key = Column(UUID, default=uuid4)
    telegram_id = Column(String)
    created = Column(DateTime, default=datetime.utcnow)
