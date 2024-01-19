from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema

auth_router = APIRouter()


@auth_router.post('/login', summary='Cria Access Token e Refresh Token', response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    # Post - usuário autenticado
    usuario = await UserService.authenticate(
        email=data.username,
        password=data.password
    )
    print(usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-email ou Senha estão incorretos'
        )
    # Criar o access_token
    return {
        "access_token": create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }

"""

Este código define uma rota POST /login usando o `APIRouter` do FastAPI. A rota recebe um objeto `OAuth2PasswordRequestForm` como parâmetro, que contém o email e a senha do usuário. Em seguida, o código chama o método `authenticate` do serviço `UserService`, passando o email e a senha fornecidos pelo usuário. Esse método é responsável por verificar se as credenciais são válidas e retorna o usuário autenticado. Se o usuário não for autenticado (ou seja, `usuario` é False), o código lança uma exceção HTTPException com o código de status 400 (Bad Request) e uma mensagem de erro. Se o usuário for autenticado com sucesso, o código retorna um objeto JSON com dois tokens: access_token e refresh_token. Esses tokens são gerados pelos métodos `create_access_token` e `create_refresh_token` do módulo `core.security`. O `access_token` é usado para autenticar as solicitações subsequentes do usuário, enquanto o `refresh_token` é usado para obter um novo `access_token` quando o atual expirar. Essa rota é usada para autenticar um usuário e fornecer os tokens necessários para acessar recursos protegidos em um aplicativo.

"""
