from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

jogadores = {
    1: {
        "nome": "Rony",
        "idade": 28,
        "time": "vasco",
    },
    2: {
        "nome": "Gustavo Gomez",
        "idade": 29,
        "time": "Palmeiras",
    }
}


class Jogador(BaseModel):
    nome: str
    idade: int
    time: str


class AtualizaJogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None

# GET #


@app.get("/")
def inicio():
    return jogadores


# Path Parameter
@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador: int):
    return jogadores[id_jogador]


# Query Parameter
@app.get("/get-jogador-time")
def get_jogador_time(time: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado"}


# POST #
@app.post("/cadastra-jogador/{jogador_id}")
def cadastra_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {"Error": "Jogador já existe"}
    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]

# DELETE #


@app.delete("/exclusao-jogador/{jogador_id}")
def exclui_jogador(jogador_id: int):
    if jogador_id not in jogadores:
        return {"Erro": "Jogador não existe"}
    del jogadores[jogador_id]
    return {"Mensagem": "Jogador excluído com sucesso"}

# PUT #


@app.put("/atualiza-jogador/{jogador_id}")
def atualiza_jogador(jogador_id: int, jogador: AtualizaJogador):
    if jogador_id not in jogadores:
        return {"Error": "Jogador não existe"}
    if jogador.nome != None:
        jogadores[jogador_id]["nome"] = jogador.nome
    if jogador.idade != None:
        jogadores[jogador_id]["idade"] = jogador.idade
    if jogador.time != None:
        jogadores[jogador_id]["time"] = jogador.time

    return jogadores[jogador_id]
