from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.user_model import User
from models.todo_model import Todo
from api.api_v1.router import router

from fastapi.middleware.cors import CORSMiddleware

# Em resumo, este código configura uma aplicação FastAPI com conexão a um banco de dados MongoDB usando a biblioteca Beanie.

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    ).todoapp

    await init_beanie(
        database=cliente_db,
        document_models=[
            # aponta os models a serem trabalhados pelo Beanie
            User,
            Todo
        ]
    )
# adição das rotas para a instáncia do FastApi
app.include_router(
    router,
    prefix=settings.API_V1_STR
)

'''
Resumindo, este código configura uma aplicação FastAPI e estabelece a conexão com um banco de dados MongoDB usando a biblioteca Beanie durante o evento de inicialização. Isso permite que a aplicação interaja com o banco de dados de maneira assíncrona e use o modelos para mapear objetos Python para documentos MongoDB.
'''
