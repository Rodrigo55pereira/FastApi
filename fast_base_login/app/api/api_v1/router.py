from fastapi import APIRouter
from api.api_v1.handlers import user
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(

    user.user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

"""
Resumindo, esse trecho de código está criando um roteador principal chamado router e incluindo um roteador adicional (user_router) dentro dele. Este roteador adicional lida com operações relacionadas a usuários e tem um prefixo "/users" para todos os seus caminhos de rota.
"""
