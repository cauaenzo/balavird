import os

# SQLite local — sem configuracao adicional necessaria
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./biblioteca.db")
