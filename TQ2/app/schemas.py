from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    pergunta: str = Field(
        ...,
        description="Pergunta do usuario sobre programacao em Python",
        json_schema_extra={"example": "Como criar uma lista em Python?"},
    )


class ChatResponse(BaseModel):
    resposta: str = Field(
        ...,
        description="Resposta detalhada gerada pelo assistente de IA",
    )
