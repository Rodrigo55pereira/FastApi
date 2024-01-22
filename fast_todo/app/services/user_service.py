from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password, verify_password
from typing import Optional
from uuid import UUID

# JWT jason web Token


class UserService:

    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username=user.username,
            email=user.email,
            hash_password=get_password(user.password)
        )
        await usuario.save()
        return usuario

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(
            password=password,
            hashed_password=user.hash_password
        ):
            return None

        return user


"""

Neste trecho de código, estamos criando uma classe chamada UserService com um método estático chamado create_user. Esse método recebe como parâmetro um objeto do tipo UserAuth, que é importado de um arquivo chamado user_schema no pacote schemas. Dentro do método create_user, estamos criando uma instância da classe User, que é importada de um arquivo chamado user_model no pacote models. Essa instância recebe os valores dos atributos username, email e hash_password, que são extraídos do objeto UserAuth passado como parâmetro. Basicamente, essa função serve para criar um novo usuário com base nas informações fornecidas no objeto UserAuth.
"""

"""
A assinatura Optional[User] é uma forma de indicar que a função pode retornar um objeto do tipo User, mas também pode retornar None se as condições no código são atendidas (por exemplo, se o usuário não for encontrado ou se a senha estiver incorreta).

Em resumo, Optional[User] indica que o retorno da função pode ser do tipo User ou None, proporcionando uma maneira explícita de indicar a possibilidade de ausência de valor.
"""
