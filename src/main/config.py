from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
from dataclasses import dataclass
from logging import getLogger
from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()
logger = getLogger(__name__)

BOT_TOKEN_ENV = "BOT_TOKEN"

REDIS_HOST_ENV = "REDIS_HOST"
REDIS_PORT_ENV = "REDIS_PORT"
REDIS_PASSWORD_ENV = "REDIS_PASSWORD"


@dataclass
class BotConfig:
    bot_token: str


@dataclass
class RedisConfig:
    host: int
    port: int
    db: str
    password: str


@dataclass
class PostgresConfig:
    user: str
    password: str
    host: int
    port: int
    db: str


def load_bot_config() -> BotConfig:
    return BotConfig(
        bot_token=os.getenv(BOT_TOKEN_ENV)
    )


def load_redis_config() -> RedisConfig:
    return RedisConfig(
        host=os.getenv("REDIS_HOST"),
        port=os.getenv("REDIS_PORT"),
        password=os.getenv("REDIS_PASSWORD") if os.getenv(
            "REDIS_PASSWORD_ENV") else None,
        db="main"
    )


def load_postgres_config() -> PostgresConfig:
    return PostgresConfig(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD") if os.getenv(
            "POSTGRES_PASSWORD") else None,
        db="hubresearcher"
    )


redis_config = load_redis_config()
redis = Redis(
    host=redis_config.host,
    port=redis_config.port
)