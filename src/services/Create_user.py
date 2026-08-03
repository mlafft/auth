from src.interfaces.Storage_Interface       import Storage_Interface
from src.entities                           import User
from src.config                             import NEW_USER
from src.models                             import UserModel

class Create_user_service ():

    def __init__ (self, storage: Storage_Interface) -> None:
        self.storage: Storage_Interface = storage
    

    def to_entity(self, user) -> User:
        return User (id=None, username=user.username, password=user.password, email=user.email)


    def to_model (self, entity) -> UserModel:
        return UserModel ( username=entity.username, password=entity.password, email=entity.email )


    async def create_user (self, schema) -> int:
        entity = self.to_entity (schema)
        result = await self.storage.add ( self.to_model(entity) )
        print (NEW_USER, result)
        return result


    async def get_user (self, id):
        result = await self.storage.get (UserModel, id)
        return result