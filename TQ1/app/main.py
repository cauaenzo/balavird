from typing import List, Optional
from app import models, schemas
from app.database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

# Cria as tabelas no banco de dados SQLite automaticamente ao iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Biblioteca Virtual",
    description=(
        "API desenvolvida para cadastro e consulta de livros em uma biblioteca"
        " virtual."
    ),
    version="1.0.0",
)


@app.post(
    "/livros/",
    response_model=schemas.LivroResponse,
    status_code=201,
    summary="Cadastrar um novo livro",
)
def cadastrar_livro(
    livro: schemas.LivroCreate, db: Session = Depends(get_db)
):
  db_livro = models.LivroModel(
      titulo=livro.titulo,
      autor=livro.autor,
      data_publicacao=livro.data_publicacao,
      resumo=livro.resumo,
  )
  db.add(db_livro)
  db.commit()
  db.refresh(db_livro)
  return db_livro


@app.get(
    "/livros/",
    response_model=List[schemas.LivroResponse],
    summary="Consultar livros por título ou autor",
)
def consultar_livros(
    titulo: Optional[str] = Query(None, description="Filtrar por título"),
    autor: Optional[str] = Query(None, description="Filtrar por autor"),
    db: Session = Depends(get_db),
):
  query = db.query(models.LivroModel)

  if titulo:
    query = query.filter(models.LivroModel.titulo.ilike(f"%{titulo}%"))
  if autor:
    query = query.filter(models.LivroModel.autor.ilike(f"%{autor}%"))

  return query.all()


@app.get(
    "/livros/{livro_id}",
    response_model=schemas.LivroResponse,
    summary="Consultar um livro específico por ID",
)
def consultar_livro_por_id(livro_id: int, db: Session = Depends(get_db)):
  livro = (
      db.query(models.LivroModel)
      .filter(models.LivroModel.id == livro_id)
      .first()
  )
  if not livro:
    raise HTTPException(status_code=404, detail="Livro não encontrado")
  return livro