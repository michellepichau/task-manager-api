"""
Script para criar todas as tabelas no banco de dados.
Execute uma vez antes de rodar a aplicação pela primeira vez.

Uso: python scripts/create_tables.py
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import Base, engine
from app.models.task import Task  # importar os models para o SQLAlchemy reconhecê-los

if __name__ == "__main__":
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")
