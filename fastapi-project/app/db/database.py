from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Cria o motor de conexão com o PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Cada instância de SessionLocal é uma sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os models
Base = declarative_base()


def get_db():
    """
    Dependency que fornece uma sessão de banco de dados para cada request.
    Fecha a sessão automaticamente ao final.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
