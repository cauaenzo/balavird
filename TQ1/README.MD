# Desafio 1 - API de Biblioteca Virtual (FastAPI)

API desenvolvida com FastAPI, SQLite, SQLAlchemy e Pydantic V2 para gerenciamento e consulta de livros.

## Como Executar

1. Crie e ative um ambiente virtual (`venv`):
   ```bash
   python -m venv venv
   ```
2. Ativação do ambiente virtual:
   ```bash
   # Windows:
   venv\Scripts\activate
   ```
   ```bash
   # Linux:
   source venv/bin/activate
   ```
3. Instalação das dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

5. Execute os testes unitários:
   ```bash
   pytest -v
   ```

6. Acesse a documentação interativa da API
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/redoc)