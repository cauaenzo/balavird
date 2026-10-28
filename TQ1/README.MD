# TQ1 - API de Biblioteca Virtual (FastAPI)

API REST para cadastro e consulta de livros, construida com FastAPI, SQLAlchemy e Pydantic v2. Persiste os dados em SQLite local.

## Estrutura

```
TQ1/
├── app/
│   ├── config.py      # Variaveis de configuracao centralizadas
│   ├── database.py    # Engine, sessao e dependencia get_db
│   ├── models.py      # Modelo ORM LivroModel
│   ├── schemas.py     # Schemas Pydantic de entrada e saida
│   └── main.py        # Endpoints FastAPI
├── tests/
│   └── test_main.py   # Testes isolados com banco em memoria
└── requirements.txt
```

## Como Executar

1. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   ```

   ```bash
   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

2. Instale as dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Execute os testes:

   ```bash
   pytest -v
   ```

5. Acesse a documentacao interativa:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Metodo | Rota              | Descricao                        |
|--------|-------------------|----------------------------------|
| POST   | `/livros/`        | Cadastra um novo livro           |
| GET    | `/livros/`        | Lista livros com filtro opcional |
| GET    | `/livros/{id}`    | Busca livro por ID               |

## Observacoes

- O banco de dados `biblioteca.db` e criado automaticamente na raiz do projeto na primeira execucao.
- Os testes usam banco SQLite em memoria e sao completamente isolados entre si.
