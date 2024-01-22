from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema, TokenPayload
from schemas.user_schema import UserDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from pydantic import ValidationError
from core.config import settings
from jose import jwt


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


@auth_router.post('/test-token', summary='Testando o Token', response_model=UserDetail)
async def test_token(user: User = Depends(get_current_user)):
    return user


@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            settings.ALGORITIMO
        )
        token_data = TokenPayload(**payload)
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='token inválido',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possível encontrar o usuário',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )

    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }

"""

Este código define uma rota POST /login usando o `APIRouter` do FastAPI. A rota recebe um objeto `OAuth2PasswordRequestForm` como parâmetro, que contém o email e a senha do usuário. Em seguida, o código chama o método `authenticate` do serviço `UserService`, passando o email e a senha fornecidos pelo usuário. Esse método é responsável por verificar se as credenciais são válidas e retorna o usuário autenticado. Se o usuário não for autenticado (ou seja, `usuario` é False), o código lança uma exceção HTTPException com o código de status 400 (Bad Request) e uma mensagem de erro. Se o usuário for autenticado com sucesso, o código retorna um objeto JSON com dois tokens: access_token e refresh_token. Esses tokens são gerados pelos métodos `create_access_token` e `create_refresh_token` do módulo `core.security`. O `access_token` é usado para autenticar as solicitações subsequentes do usuário, enquanto o `refresh_token` é usado para obter um novo `access_token` quando o atual expirar. Essa rota é usada para autenticar um usuário e fornecer os tokens necessários para acessar recursos protegidos em um aplicativo.

* O access_token é como uma chave temporária que permite o acesso aos recursos protegidos da aplicação.

* O refresh_token é usado para obter um novo access_token quando o antigo expira, evitando que o usuário tenha que fazer login repetidamente.

* Depends(get_current_user)

Quando um cliente faz uma requisição para a rota /test-token com um método POST, a função test_token é chamada.

Antes de executar a lógica da função test_token, o FastAPI executa a função get_current_user devido ao Depends.

O resultado da função get_current_user (que geralmente é um usuário autenticado) é passado como argumento para a função test_token.

A função test_token é então executada com o usuário retornado pela função de dependência, e o resultado da função é retornado como resposta da rota.

O uso de Depends permite uma injeção de dependência limpa e modular, facilitando a organização do código e a reutilização de lógicas comuns em diferentes rotas. No exemplo fornecido, a função get_current_user provavelmente é responsável por verificar a autenticidade do token na requisição e retornar o usuário associado a esse token.

"""
