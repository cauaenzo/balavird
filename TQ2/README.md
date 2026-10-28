# TQ2 - Chatbot Python (FastAPI & LangChain)

API REST para um assistente especialista em programacao Python, construida com FastAPI e LangChain. Integra com a API da OpenAI (ou compativel) e disponibiliza uma CLI interativa para testes via terminal.

## Estrutura

```
TQ2/
├── app/
│   ├── config.py              # Leitura de variaveis de ambiente centralizada
│   ├── schemas.py             # Schemas Pydantic de entrada e saida
│   ├── main.py                # Endpoint FastAPI
│   └── services/
│       └── chatbot_service.py # Chain LangChain e logica de resposta
├── tests/
│   └── test_chatbot.py        # Testes com mock do servico de IA
├── run_cli.py                 # CLI interativa
├── .env.example               # Modelo de variaveis de ambiente
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

3. Configure as variaveis de ambiente:

   ```bash
   # Windows
   copy .env.example .env

   # Linux / macOS
   cp .env.example .env
   ```

   Edite o `.env` e preencha `OPENAI_API_KEY` com sua chave.

4. Inicie o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Execute a CLI interativa:

   ```bash
   python run_cli.py
   ```

6. Execute os testes:

   ```bash
   pytest -v
   ```

7. Acesse a documentacao interativa:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Variaveis de Ambiente

| Variavel          | Descricao                             | Padrao                        |
|-------------------|---------------------------------------|-------------------------------|
| `OPENAI_API_KEY`  | Chave de autenticacao da API (obrigatorio) | —                         |
| `OPENAI_BASE_URL` | URL base da API OpenAI ou compativel  | `https://api.openai.com/v1`   |
| `MODEL_NAME`      | Modelo a ser utilizado                | `gpt-4o-mini`                 |
