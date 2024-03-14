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


def load_bot_config() -> BotConfig:
    return BotConfig(
        bot_token=os.getenv(BOT_TOKEN_ENV)
    )
    
    
def load_redis_config() -> RedisConfig:
    return RedisConfig(
        host=os.getenv("REDIS_HOST_ENV"),
        port=os.getenv("REDIS_PORT_ENV"),
        password=os.getenv("REDIS_PASSWORD_ENV") if os.getenv("REDIS_PASSWORD_ENV") else None, 
        db="main"
    )
    
 
redis_config = load_redis_config()   
redis = Redis(
    host=redis_config.host, 
    port=redis_config.port
)