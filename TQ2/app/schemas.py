from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
  pergunta: str = Field(
      ...,
      description="Pergunta do usuário sobre programação em Python",
      example="Como criar uma lista em Python?",
  )


class ChatResponse(BaseModel):
  resposta: str = Field(
      ...,
      description="Resposta detalhada gerada pelo assistente de IA",
  )