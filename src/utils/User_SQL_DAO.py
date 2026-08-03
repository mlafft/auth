from src.interfaces.Storage_Interface       import Storage_Interface
from src.models                             import Model
from src.database                           import session_maker
from src.models                             import UserModel


class User_SQL_DAO (Storage_Interface):


    def to_model (self, entity) -> UserModel:
            return UserModel ( username=entity.username, password=entity.password, email=entity.email )
    

    async def add (self, entity) -> int:
        async with session_maker () as trans:

            model = self.to_model(entity)

            try:
                trans.add (model)
                await trans.commit ()
                await trans.refresh (model)
                return model.id
                
            except Exception as error:
                print (error) 
                return 0   
            
    
    async def get (self, model_type, id) -> Model | None | int: 
        async with session_maker () as trans:

            try:
                model = await trans.get (model_type, id)
                
                if not model:
                    return None
                    
                return model
    
            except Exception as error:
                await trans.rollback ()
                print (error)
                return 0
