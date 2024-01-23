from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    # Indexed que dizer que o valor deve ser unico
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hash_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

    # Facilita a depuração do código

    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(self, email: str) -> "User":
        return await self.find_one(self.email == email)


'''
Em resumo, este código define uma classe User usando Beanie e Pydantic para interagir com um banco de dados MongoDB. Ele inclui campos obrigatórios e opcionais, métodos especiais para representação textual e comparação, e métodos para realizar operações específicas, como encontrar um usuário por e-mail.
'''
