from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão com o banco de dados SQLite local
SQLALCHEMY_DATABASE_URL = "sqlite:///./biblioteca.db"

# Criação do engine do SQLAlchemy (check_same_thread é necessário para o SQLite no FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fábrica de sessões para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa atualizada para o SQLAlchemy 2.0
Base = declarative_base()


# Função utilitária para obter a sessão do banco por requisição
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()