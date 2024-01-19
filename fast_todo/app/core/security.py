from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password(password: str) -> str:
    # print(password_context.hash(password))
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.uctnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITIMO
    )

    return jwt_encoded


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.uctnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITIMO
    )

    return jwt_encoded


"""
Este código Python utiliza a biblioteca passlib para lidar com a segurança de senhas, especialmente usando o esquema de hash 'bcrypt'.

Em resumo, este código fornece uma maneira de criar hashes seguros para senhas e verificar se uma senha em texto plano corresponde a um hash previamente armazenado. Ele utiliza o algoritmo de hash 'bcrypt' para garantir uma segurança adequada.

Esta função `create_access_token` cria um token de acesso JWT (JSON Web Token) usando a biblioteca `jwt` em Python. Possui dois parâmetros: `subject` e `expires_delta`. - `subject` é uma string ou qualquer outro objeto, ele é convertido em uma string usando `str(subject)`. - `expires_delta` é um valor inteiro opcional que representa a quantidade de tempo, em segundos, que o token permanecerá válido. Se este valor não for fornecido, o valor armazenado em `settings.ACCESS_TOKEN_EXPIRE_MINUTES` será usado para determinar a expiração do token. A partir disso, o código faz o seguinte:

1. Se `expires_delta` não for `None`, a data e hora de expiração são calculadas adicionando `expires_delta` à hora atual com `datetime.utcnow() + expires_delta`. Se `None`, a hora atual mais `settings.ACCESS_TOKEN_EXPIRE_MINUTES` minutos serão usados.

2. Um dicionário chamado `info_jwt` é criado com duas chaves: "exp" (tempo de expiração) e "sub" (assunto). O tempo de expiração é definido como o valor calculado na etapa anterior e o assunto é definido como a representação de string de `assunto`.

3. O dicionário `info_jwt` é codificado em um token JWT usando a função `jwt.encode()`. `settings.JWT_SECRET_KEY` é usado como chave secreta e `settings.ALGORITIMO` é usado como algoritmo de criptografia. 4. O token JWT codificado é retornado como resultado da função.

"""
