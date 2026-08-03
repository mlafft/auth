from fastapi                    import Depends
from typing                     import Annotated
from sqlalchemy.ext.asyncio     import AsyncSession

from src.services.Create_user   import Create_user_service
from src.utils.User_SQL_DAO     import User_SQL_DAO
from src.database               import get_session


def get_create_user_service () -> Create_user_service:
    return Create_user_service( User_SQL_DAO() )

Service_dep = Annotated[Create_user_service, Depends (get_create_user_service)]

Session_dep = Annotated[AsyncSession, Depends (get_session)]
