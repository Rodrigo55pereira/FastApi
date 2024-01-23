from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from fastapi import Depends, HTTPException, status
from models.user_model import User
from jose import jwt
from schemas.auth_schema import TokenPayload
from datetime import datetime
from pydantic import ValidationError
from services.user_service import UserService

oauth_reusavel = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITIMO
        )
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token foi expirado',
                headers={'WWW-Authenticate': 'Bearer'}
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Error na validação do token',
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

    return user

"""
O código fornecido mostra uma função `get_current_user` que é usada para obter o usuário atual com base em um token de autenticação fornecido. A autenticação é feita usando o esquema OAuth2PasswordBearer fornecido pela FastAPI. O objeto `oauth_reusavel` é uma instância de `OAuth2PasswordBearer` que é usada como uma dependência da função `get_current_user`. Este objeto é configurado com a URL de solicitação do token e o nome do esquema (neste caso, “JWT”). A função `get_current_user` recebe um token como parâmetro e realiza diversas verificações para validar e decodificar o token. Use o módulo `jose` para decodificar o token usando a chave secreta e o algoritmo definidos nas configurações do aplicativo. A expiração do token é então verificada comparando a data de expiração na carga útil do token com a data e hora atuais. Se o token expirou, uma exceção HTTP 401 será gerada com uma mensagem indicando que o token expirou. Caso ocorra um erro na decodificação ou validação do token, uma exceção HTTP 403 é gerada com uma mensagem indicando que ocorreu um erro de validação do token. Resumindo, esta função é usada como uma dependência para obter o usuário atual com base em um token de autenticação. Verifica a validade e expiração do token antes de retornar o usuário correspondente.

"""
