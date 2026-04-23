from src.api                import api_router
from src.auth               import auth_router
from fastapi.templating     import Jinja2Templates
from fastapi                import APIRouter

router = APIRouter ()

router.include_router (api_router)
router.include_router (auth_router)

templates = Jinja2Templates (directory="./templates")
