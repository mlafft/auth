import uvicorn

from fastapi                 import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles     import StaticFiles
from fastapi.responses       import JSONResponse
from authx.exceptions        import MissingTokenError
from contextlib              import asynccontextmanager
from src                     import router
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


app = FastAPI (lifespan=lifecycle)
app.include_router (router)
app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_methods=["POST", "OPTIONS"] )
app.mount ( "/static", StaticFiles(directory="./static"), name="static" )


@app.exception_handler (MissingTokenError)
async def handle_missing_token (request: Request, exc: MissingTokenError):
    return JSONResponse( status_code=401, content={"detail": "Token required"} )


if __name__ == "__main__":
    uvicorn.run( "src.main:app", reload=True, host='0.0.0.0', port=3000 )
