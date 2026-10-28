import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# StaticPool garante que todas as threads usam a mesma conexao em memoria.
# Sem isso, cada thread ve um banco vazio — comportamento padrao do SQLite :memory:.
engine_test = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


@pytest.fixture()
def client():
    Base.metadata.create_all(bind=engine_test)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine_test)


_LIVRO_PAYLOAD = {
    "titulo": "Arquitetura Limpa",
    "autor": "Robert C. Martin",
    "data_publicacao": "2019-03-15",
    "resumo": "Um guia sobre o design de software.",
}


def test_cadastrar_livro(client):
    response = client.post("/livros/", json=_LIVRO_PAYLOAD)
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Arquitetura Limpa"
    assert "id" in data


def test_consultar_livros_por_autor(client):
    client.post("/livros/", json=_LIVRO_PAYLOAD)
    response = client.get("/livros/?autor=Martin")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["autor"] == "Robert C. Martin"


def test_consultar_livro_por_id_sucesso(client):
    post = client.post("/livros/", json=_LIVRO_PAYLOAD)
    livro_id = post.json()["id"]

    response = client.get(f"/livros/{livro_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Arquitetura Limpa"


def test_consultar_livro_por_id_nao_encontrado(client):
    response = client.get("/livros/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Livro nao encontrado"
