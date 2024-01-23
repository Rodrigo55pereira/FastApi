from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from models.user_model import User


class Todo(Document):
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str)
    description: Indexed(str)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    # cria um agregado dentro de outro - relacionamento (para que entenda que é o dono, no caso o usuário)
    owner: Link[User]

    # Funções Auxiliares
    def __repr__(self) -> str:
        return f"<Todo {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Todo):
            return self.todo_id == other.todo_id
        return False

    # Evento que verifica se ouve alterações sempre se tiver um Replace ou um Insert e em seguida atualiza updated_at com a data atual.
    @before_event([Replace, Insert])
    def sync_update_at(self):
        self.updated_at = datetime.utcnow()
