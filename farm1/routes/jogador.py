from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador

jogador_router = APIRouter()


@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao FullStack Farm"

@jogador_router.get("/jogadores")
async def lista_jogadores():
    return conexao.local.jogador.find()
