from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

# Em resumo, este código configura uma aplicação FastAPI com conexão a um banco de dados MongoDB usando a biblioteca Beanie.

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    ).todoapp

    await init_beanie(
        database=cliente_db,
        document_models=[

        ]
    )
