from abc                                    import abstractmethod
from dataclasses                            import dataclass
from src.infrastructure.Entity_interface    import Entity_interface
from src.models                             import UserModel


@dataclass
class User ():

    id: int | None
    email: str
    username: str
    password: str
