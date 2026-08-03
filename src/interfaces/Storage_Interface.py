from abc                                    import ABC, abstractmethod
from src.models                             import Model


class Storage_Interface (ABC):

    @abstractmethod
    async def add (self, entity) -> int:
        raise NotImplementedError
    

    @abstractmethod
    async def get (self, model_type, id: int) -> Model | None | int:
        raise NotImplementedError
