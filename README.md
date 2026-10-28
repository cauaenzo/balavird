# balavird

Repositório com três projetos independentes em Python, cada um cobrindo uma camada diferente do desenvolvimento backend moderno: persistência relacional via ORM, integração com modelos de linguagem e busca semântica local com vetores densos.

---

## Projetos

### TQ1 - API de Biblioteca Virtual

API REST construída com FastAPI, SQLAlchemy e Pydantic v2 para cadastro e consulta de livros em uma biblioteca virtual. Persiste dados em SQLite local via ORM e expõe endpoints de criação e busca com filtros por título e autor.

Acesse: [`TQ1/README.MD`](TQ1/README.MD)

---

### TQ2 - Chatbot Python

API REST com FastAPI integrada ao LangChain e à API da OpenAI para um assistente especialista em programação Python. Inclui uma CLI interativa para testes rápidos via terminal sem necessidade de subir o servidor.

Acesse: [`TQ2/README.md`](TQ2/README.md)

---

### TQ3 - Busca Semântica com FAISS

Sistema de busca semântica local que indexa artigos do dataset público `fancyzhx/ag_news` usando o modelo `all-MiniLM-L6-v2` para geração de embeddings densos, persiste o índice vetorial com FAISS e expõe uma interface de busca por similaridade via CLI.

Acesse: [`TQ3/README.md`](TQ3/README.md)

---

Cada projeto possui seu próprio `venv`, `requirements.txt` e instruções de execução no README interno. Não há dependências cruzadas entre eles.

---

## Requisitos Gerais

- Python 3.11 ou superior
- pip atualizado (`pip install --upgrade pip`)
- Conexão com a internet para download de modelos e datasets na primeira execução (TQ2 e TQ3)
