import uvicorn

from fastapi                 import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles     import StaticFiles
from fastapi.responses       import JSONResponse
from authx.exceptions        import MissingTokenError
from src                     import router
from src.services.lifecycle  import lifecycle


app = FastAPI (lifespan=lifecycle)

app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_methods=["POST", "OPTIONS"] )
app.mount ( "/static", StaticFiles(directory="./static"), name="static" )
app.include_router (router)


@app.exception_handler (MissingTokenError)
async def handle_missing_token (request: Request, exc: MissingTokenError):
    return JSONResponse( status_code=401, content={"detail": "Token required"} )


if __name__ == "__main__":
    uvicorn.run( "src.main:app", reload=True, port=3000 )
