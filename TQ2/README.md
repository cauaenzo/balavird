# Desafio 2 - Chatbot Python (FastAPI & LangChain)

API moderna, modular e segura desenvolvida em **FastAPI** integrada ao **LangChain** para criação de um assistente especialista em programação Python. O projeto também conta com uma ferramenta CLI interativa para testes rápidos via terminal.

## Como Executar

. Crie e ative um ambiente virtual (`venv`):
   ```bash
   python -m venv venv
   ```
. Ativação do ambiente virtual:
   ```bash
   # Windows:
   venv\Scripts\activate
   ```
   ```bash
   # Linux:
   source venv/bin/activate
   ```
. Instalação das dependências:
   ```bash
   pip install -r requirements.txt
   ```
. Configurando o env (coloque sua chave de API do OpenAI no arquivo .env e certifique-se que está correta, caso contrário a API não funcionará):
   ```pwsh
   # Windows:
   copy .env.example .env
   ```
   ```pwsh
   # Linux:
   cp .env.example .env
   ```
. Execute o servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

. Execute os testes unitários:
   ```bash
   pytest -v
   ```

. Acesse a documentação interativa da API
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/redoc)