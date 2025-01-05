from pydantic import BaseModel, Field
from typing import Optional

class Todo(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., title="Título", max_length=100)
    description: Optional[str] = Field(None, title="Descrição", max_length=450)
    completed: bool = Field(False, title="Tarefa Concluída")
