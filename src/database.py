from src.dependencies import Engine_dep

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.models             import Model
from src.config             import DB_URL


async_engine  = create_async_engine (f"postgresql+asyncpg://{DB_URL}")
session_maker = async_sessionmaker (async_engine, expire_on_commit=False)


async def init_db (conn: Engine_dep):
    await conn.run_sync (Model.metadata.create_all)
    

async def reset_db (conn: Engine_dep):
    await conn.run_sync (Model.metadata.drop_all)
    

async def get_session ():
    
    async with session_maker () as trans:
        yield trans


async def get_engine ():
    
    async with async_engine.begin () as conn:
        yield conn
