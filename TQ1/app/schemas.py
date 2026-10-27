from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class LivroBase(BaseModel):
  titulo: str = Field(..., json_schema_extra={"example": "Python Fluente"})
  autor: str = Field(..., json_schema_extra={"example": "Luciano Ramalho"})
  data_publicacao: date = Field(
      ..., json_schema_extra={"example": "2015-08-25"}
  )
  resumo: Optional[str] = Field(
      None,
      json_schema_extra={
          "example": "Guia definitivo para programação em Python."
      },
  )


class LivroCreate(LivroBase):
  pass


class LivroResponse(LivroBase):
  id: int

  model_config = ConfigDict(from_attributes=True)