from fastapi                import APIRouter, HTTPException,Response
from sqlalchemy             import select
from src.dependencies       import Session_dep
from src.models             import UserModel
from src.schemas            import UserDataSchema
from src.config             import security
from src.dependencies       import Service_dep


router = APIRouter ()

@router.post ('/regestration', summary='запись', tags=['Auth'])
async def regestration (credentials: UserDataSchema, service: Service_dep):
    
    result = await service.create_user (credentials)
    return {'id': result}


@router.post ('/authentication', summary='вход', tags=['Auth'])
async def login  (credentials: UserDataSchema, session: Session_dep, response: Response):
    
    query = select (UserModel).where (UserModel.password == credentials.password)
    result = await session.execute (query)
    user = result.scalar ()

    print (user)

    if user is None or credentials.username != user.username:
        raise HTTPException( status_code=401, detail='Неверное имя пользователя' )
    
    if credentials.password != user.password:
        raise HTTPException( status_code=401, detail='Неверный пароль' )
    
    token = security.create_access_token (uid=f"{user.id}")
    response.set_cookie( security.config.JWT_ACCESS_COOKIE_NAME, token )
    return {"access_token": token}