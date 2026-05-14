from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def get_task(db: Session, task_id: int):
    """Busca uma task pelo ID. Retorna None se não encontrar."""
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """Retorna lista de tasks com paginação."""
    return db.query(Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: TaskCreate):
    """Cria uma nova task no banco."""
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)  # atualiza o objeto com os dados gerados pelo banco (ex: id)
    return db_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    """Atualiza apenas os campos enviados (PATCH)."""
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    # exclude_unset=True garante que só campos enviados na requisição sejam atualizados
    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """Remove uma task do banco. Retorna True se deletou, False se não encontrou."""
    db_task = get_task(db, task_id)
    if not db_task:
        return False
    db.delete(db_task)
    db.commit()
    return True
