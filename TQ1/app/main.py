from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Biblioteca Virtual",
    description=(
        "API desenvolvida para cadastro e consulta de livros em uma biblioteca virtual."
    ),
    version="1.0.0",
)


def _get_livro_or_404(db: Session, livro_id: int) -> models.LivroModel:
    livro = db.query(models.LivroModel).filter(models.LivroModel.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro nao encontrado")
    return livro


@app.post(
    "/livros/",
    response_model=schemas.LivroResponse,
    status_code=201,
    summary="Cadastrar um novo livro",
)
def cadastrar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
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
    summary="Consultar livros por titulo ou autor",
)
def consultar_livros(
    titulo: Optional[str] = Query(None, description="Filtrar por titulo"),
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
    summary="Consultar um livro especifico por ID",
)
def consultar_livro_por_id(livro_id: int, db: Session = Depends(get_db)):
    return _get_livro_or_404(db, livro_id)
