from pydantic       import BaseModel, ConfigDict, EmailStr, Field


class UserDataSchema (BaseModel):
    username: str = Field (min_length=2, max_length=28)
    password: str = Field (min_length=8, max_length=20)
    email: EmailStr 

    model_config = ConfigDict (extra='forbid', frozen=True)