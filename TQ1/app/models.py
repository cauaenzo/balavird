from app.database import Base
from sqlalchemy import Column, Date, Integer, String


class LivroModel(Base):
  __tablename__ = "livros"

  id = Column(Integer, primary_key=True, index=True)
  titulo = Column(String, index=True, nullable=False)
  autor = Column(String, index=True, nullable=False)
  data_publicacao = Column(Date, nullable=False)
  resumo = Column(String, nullable=True)