from fastapi                import APIRouter

from src.api                import api_router
from src.api.front          import front_router
from src.auth               import auth_router


router = APIRouter ()

router.include_router (front_router)
router.include_router (api_router)
router.include_router (auth_router)
