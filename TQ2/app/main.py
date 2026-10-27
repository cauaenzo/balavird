from app import schemas
from app.services.chatbot_service import gerar_resposta_chatbot
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Chatbot Python (LangChain)",
    description=(
        "API desenvolvida para responder dúvidas de programação em Python"
        " utilizando LangChain e LLM."
    ),
    version="1.0.0",
)


@app.post(
    "/chat/",
    response_model=schemas.ChatResponse,
    summary="Enviar pergunta para o chatbot de Python",
)
def conversar_com_chatbot(payload: schemas.ChatRequest):
  try:
    resposta_ia = gerar_resposta_chatbot(payload.pergunta)
    return {"resposta": resposta_ia}
  except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=f"Erro ao processar a resposta do LLM: {str(e)}",
    )