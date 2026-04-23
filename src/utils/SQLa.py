from src.infrastructure.Storage_Interface   import Storage_Interface
from src.models                             import Model
from src.database                           import session


class SQLa (Storage_Interface):

    async def add (self, model) -> int:
        async with session () as trans:

            try:
                trans.add (model)
                await trans.commit ()
                await trans.refresh (model)
                return model.id
                
            except Exception as error:
                print (error) 
                return 0   
            
    
    async def get (self, model_type, id) -> Model | None | int: 
        async with session () as trans:

            try:
                model = await trans.get (model_type, id)
                
                if not model:
                    return None
                    
                return model
    
            except Exception as error:
                await trans.rollback ()
                print (error)
                return 0
