from fastapi                import APIRouter, Depends
from sqlalchemy             import select
from src.dependencies       import SessionDep, Service_dep
from src.models             import UserModel
from src.config             import security

router = APIRouter ()

@router.get( '/protected', dependencies=[Depends(security.access_token_required)], summary="доступ", tags=['API'] )
async def protected ():
    return {"access": True}


@router.get( '/users', summary="список пользователей", tags=['API'] )
async def list (session: SessionDep):
    
    query  = select (UserModel)
    result = await session.execute (query)
    return result.scalars().all ()


@router.get( '/user/{id}', summary="пользователь", tags=['API'] )
async def user (id: int, service: Service_dep):
    result = await service.get_user (id)
    return result