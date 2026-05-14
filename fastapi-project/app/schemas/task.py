from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    """Campos compartilhados entre criação e atualização."""
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Schema para criar uma task — só precisa do title obrigatório."""
    pass


class TaskUpdate(BaseModel):
    """Schema para atualizar — todos os campos são opcionais."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(TaskBase):
    """Schema de resposta — inclui campos gerados pelo banco."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # permite converter model SQLAlchemy → Pydantic
