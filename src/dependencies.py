from fastapi                    import Depends
from typing                     import Annotated
from sqlalchemy.ext.asyncio     import AsyncSession
from src.database               import get_session
from src.services.Create_user   import Create_user_service
from src.utils.SQLa             import SQLa


SessionDep = Annotated[AsyncSession, Depends (get_session)]


def get_create_user_service () -> Create_user_service:
    return Create_user_service( SQLa() )

Service_dep = Annotated[Create_user_service, Depends (get_create_user_service)]
