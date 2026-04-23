from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.models             import Model
from src.config             import DB_URL


engine    = create_async_engine (f"postgresql+asyncpg://{DB_URL}")
session   = async_sessionmaker (engine, expire_on_commit=False)


async def init_db ():
    async with engine.begin () as conn:
        await conn.run_sync (Model.metadata.create_all)

async def reset_db ():
    async with engine.begin () as conn:
        await conn.run_sync (Model.metadata.drop_all)

async def get_session ():
    async with session () as trans:
        yield trans
