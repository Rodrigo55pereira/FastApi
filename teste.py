from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

'''
@app.get("/")
def root():
    return {'mensagem': 'home'}


@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'cadstro'}


@app.get("/login")
def login():
    return {'mensagem': 'login'}
'''

usuarios = [(1, 'caio', 'minhasenha1'), (2, 'joao', 'minhasenha2')]

'''
@app.get('/usuario/{id}')
def main(id: int):
    for i in usuarios:
        if i[0] == id:
            return i
    return "Não existe esse usuário"
'''

'''
@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    return "Não existe esse usuário"
'''


class Usuario(BaseModel):
    id: int
    nome: Optional[str]
    senha: str


lista = [
    Usuario(id=1, nome='caio', senha='minhasenha1'),
    Usuario(id=2, nome='marcos', senha='minhasenha2'),
    Usuario(id=3, nome='joao', senha='minhasenha3')
]

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)
    return "usuário cadastrado"

@app.get('/usuarioListar')
def main():
    return lista