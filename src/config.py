import os

from authx              import AuthX, AuthXConfig
from pydantic_settings  import BaseSettings


config = AuthXConfig ()
config.JWT_SECRET_KEY           = '1232-6432-8890-1110-AQSL-8888-M1AX'
config.JWT_ACCESS_COOKIE_NAME   = 'acces_token_config'
config.JWT_TOKEN_LOCATION       = ['cookies']
security = AuthX (config=config)


RESET  = "\033[0m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"

START    = f"{YELLOW}WARNING{RESET}:  Запуск.."
READY    = f"{GREEN}INFO{RESET}:     База готова."
STOP     = f"{YELLOW}WARNING{RESET}:  Остановка.."
NEW_USER = f"{GREEN}INFO{RESET}:     Заргестрирован новый пользователь c ID "

DB_URL = os.getenv ('DB_URL')


class Settings (BaseSettings):

    PG_HOST:        str | None = os.getenv ('PG_HOST')
    PG_PORT:        str | None = os.getenv ('PG_PORT')
    PG_USER:        str | None = os.getenv ('PG_USER')
    PG_PASS:        str | None = os.getenv ('PG_PASS')
    PG_NAME:        str | None = os.getenv ('PG_NAME')
    DB_DIALECT:     str | None = "postgresql+asyncpg"

    # model_config = {"env_file": ".env"}
    

    @property
    def db_url(self) -> str:
        return (f"{self.DB_DIALECT}://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:"f"{self.PG_PORT}/{self.PG_NAME}")
    
    # @property
    # def my_print (self):
    #     print (self.PG_HOST)


settings = Settings ()
