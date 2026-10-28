from unittest.mock import patch
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@patch("app.main.gerar_resposta_chatbot")
def test_conversar_com_chatbot_sucesso(mock_gerar_resposta):
  # Simula o retorno do serviço de IA do LangChain
  mock_gerar_resposta.return_value = (
      "Para criar uma lista em Python, você pode usar colchetes, por exemplo:"
      " minha_lista = [1, 2, 3]."
  )

  payload = {"pergunta": "Como criar uma lista em Python?"}
  response = client.post("/chat/", json=payload)

  # Validações
  assert response.status_code == 200
  data = response.json()
  assert "resposta" in data
  assert "lista em Python" in data["resposta"]
  mock_gerar_resposta.assert_called_once_with("Como criar uma lista em Python?")


def test_conversar_com_chatbot_payload_invalido():
  # Testa se o Pydantic rejeita uma requisição sem o campo 'pergunta'
  response = client.post("/chat/", json={})

  assert response.status_code == 422  # Erro de validação padrão do FastAPI