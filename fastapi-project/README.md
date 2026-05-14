# Task Manager API 📋

API REST de gerenciamento de tarefas construída com **FastAPI** e **PostgreSQL**. Projeto desenvolvido para praticar desenvolvimento backend Python com foco em APIs escaláveis, banco de dados relacional e containerização com Docker.

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

## 📐 Arquitetura do projeto

```
task-manager-api/
│
├── app/
│   ├── api/v1/endpoints/
│   │   └── tasks.py        # rotas da API (GET, POST, PATCH, DELETE)
│   │
│   ├── core/
│   │   ├── config.py       # configurações e variáveis de ambiente
│   │   └── security.py     # JWT e hash de senha
│   │
│   ├── db/
│   │   └── database.py     # conexão com PostgreSQL via SQLAlchemy
│   │
│   ├── models/
│   │   └── task.py         # model da tabela 'tasks' no banco
│   │
│   ├── schemas/
│   │   └── task.py         # validação de dados com Pydantic
│   │
│   ├── services/
│   │   └── task_service.py # lógica de negócio (CRUD)
│   │
│   └── main.py             # inicialização da aplicação FastAPI
│
├── tests/
│   └── test_tasks.py       # testes automatizados com pytest
│
├── scripts/
│   └── create_tables.py    # script para criar tabelas no banco
│
├── .github/workflows/
│   └── ci.yml              # pipeline CI com GitHub Actions
│
├── docker-compose.yml      # orquestra API + PostgreSQL
├── Dockerfile              # imagem da aplicação
├── requirements.txt        # dependências Python
└── .env.example            # modelo de variáveis de ambiente
```

## ✨ Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/v1/tasks/` | Lista todas as tasks |
| `GET` | `/api/v1/tasks/{id}` | Busca task por ID |
| `POST` | `/api/v1/tasks/` | Cria nova task |
| `PATCH` | `/api/v1/tasks/{id}` | Atualiza task parcialmente |
| `DELETE` | `/api/v1/tasks/{id}` | Remove task |
| `GET` | `/health` | Health check da API |
| `GET` | `/docs` | Documentação Swagger interativa |

## 🚀 Como rodar

### Com Docker (recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/michellepichau/task-manager-api.git
cd task-manager-api

# 2. Copie o arquivo de variáveis de ambiente
cp .env.example .env

# 3. Suba os containers (API + PostgreSQL)
docker compose up --build

# 4. Acesse a API
# Swagger: http://localhost:8000/docs
# Health:  http://localhost:8000/health
```

### Sem Docker (ambiente local)

```bash
# 1. Clone e entre na pasta
git clone https://github.com/michellepichau/task-manager-api.git
cd task-manager-api

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# edite o .env com suas credenciais do PostgreSQL local

# 5. Crie as tabelas no banco
python scripts/create_tables.py

# 6. Suba a aplicação
uvicorn app.main:app --reload

# Acesse: http://localhost:8000/docs
```

## 🧪 Testes

```bash
# Roda todos os testes
pytest tests/ -v

# Com cobertura de código
pytest tests/ -v --cov=app
```

Os testes usam SQLite em memória — sem necessidade de PostgreSQL rodando.

## 📚 O que este projeto pratica

- **FastAPI** — criação de APIs REST com documentação automática (Swagger/ReDoc)
- **SQLAlchemy** — ORM para modelagem e consulta ao banco de dados
- **PostgreSQL** — banco de dados relacional em produção
- **Pydantic** — validação de dados de entrada e saída
- **Docker & Docker Compose** — containerização da aplicação e do banco
- **Pytest** — testes automatizados com banco isolado
- **GitHub Actions** — CI rodando testes a cada push

## 👩‍💻 Autora

**Michelle Pichau** — [GitHub](https://github.com/michellepichau) · [LinkedIn](https://linkedin.com/in/michellepichau)
