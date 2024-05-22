from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import database_config

engine = create_async_engine(database_config.url)

async_session = async_sessionmaker(engine, expire_on_commit=False)
