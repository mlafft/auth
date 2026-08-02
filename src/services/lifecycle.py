from fastapi                 import FastAPI
from contextlib              import asynccontextmanager
from src.database            import init_db, reset_db
from src.config              import START, READY, STOP


@asynccontextmanager
async def lifecycle (app: FastAPI):
    print (START)
    await init_db ()
    print (READY)
    yield

    await reset_db ()
    print (STOP)
