from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.main.config import load_postgres_config


pg_config = load_postgres_config()

DATABASE_URL = (
    "postgresql://%s:%s@%s/%s" % (
        pg_config.user,
        pg_config.password,
        pg_config.host,
        pg_config.db
    )
)


engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


def init_models():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)


def get_session() -> Session:
    return Session()
