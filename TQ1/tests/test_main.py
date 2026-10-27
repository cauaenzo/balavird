from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_cadastrar_livro():
  response = client.post(
      "/livros/",
      json={
          "titulo": "Arquitetura Limpa",
          "autor": "Robert C. Martin",
          "data_publicacao": "2019-03-15",
          "resumo": "Um guia sobre o design de software.",
      },
  )
  assert response.status_code == 201
  data = response.json()
  assert data["titulo"] == "Arquitetura Limpa"
  assert "id" in data


def test_consultar_livros():
  response = client.get("/livros/?autor=Martin")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, list)
  assert len(data) > 0
  assert data[0]["autor"] == "Robert C. Martin"


def test_consultar_livro_por_id_sucesso():
  # Busca o livro com ID 1 cadastrado nos testes anteriores
  response = client.get("/livros/1")
  assert response.status_code == 200
  data = response.json()
  assert data["id"] == 1
  assert data["titulo"] == "Arquitetura Limpa"


def test_consultar_livro_por_id_nao_encontrado():
  # Busca por um ID inexistente
  response = client.get("/livros/9999")
  assert response.status_code == 404
  assert response.json()["detail"] == "Livro não encontrado"