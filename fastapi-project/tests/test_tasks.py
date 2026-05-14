import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_db():
    """Cria e destrói as tabelas a cada teste — garante isolamento."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_criar_task():
    response = client.post("/api/v1/tasks/", json={"title": "Estudar FastAPI"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Estudar FastAPI"
    assert data["completed"] is False
    assert "id" in data


def test_listar_tasks():
    client.post("/api/v1/tasks/", json={"title": "Task 1"})
    client.post("/api/v1/tasks/", json={"title": "Task 2"})
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_buscar_task_por_id():
    criada = client.post("/api/v1/tasks/", json={"title": "Minha task"}).json()
    response = client.get(f"/api/v1/tasks/{criada['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Minha task"


def test_buscar_task_inexistente():
    response = client.get("/api/v1/tasks/9999")
    assert response.status_code == 404


def test_atualizar_task():
    criada = client.post("/api/v1/tasks/", json={"title": "Antes"}).json()
    response = client.patch(
        f"/api/v1/tasks/{criada['id']}",
        json={"title": "Depois", "completed": True},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Depois"
    assert response.json()["completed"] is True


def test_deletar_task():
    criada = client.post("/api/v1/tasks/", json={"title": "Deletar"}).json()
    response = client.delete(f"/api/v1/tasks/{criada['id']}")
    assert response.status_code == 204
    # confirma que sumiu
    assert client.get(f"/api/v1/tasks/{criada['id']}").status_code == 404
