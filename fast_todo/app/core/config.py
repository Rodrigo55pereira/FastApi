from typing import List
from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

# AnyHttpUrl serve para validar se a URLs passadas são validas.
#


class Settings(BaseSettings):
    # Prefixo (denominando nome para a API com sua versão).
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITIMO: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 dias
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "TODOFast"

    # DataBase
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()

'''
Resumindo, esse código utiliza Pydantic e Decouple para definir e carregar configurações da aplicação, incluindo informações importantes como chaves secretas, tempos de expiração e informações de banco de dados. Essas configurações podem ser facilmente ajustadas e acessadas em outros módulos do código.
'''
