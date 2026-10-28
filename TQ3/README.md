# TQ3 - Busca Semantica com FAISS e Sentence Transformers

API de busca semantica que indexa artigos do dataset publico `fancyzhx/ag_news` (Hugging Face) usando o modelo `all-MiniLM-L6-v2` para gerar embeddings densos, persiste o indice vetorial com FAISS e expoe uma interface de busca por similaridade via CLI.

## Estrutura

```
TQ3/
├── app/
│   ├── config.py            # Constantes e caminhos centralizados
│   ├── embedding_service.py # Carregamento do dataset, geracao de embeddings e persistencia
│   └── search_service.py    # Busca vetorial no indice FAISS
├── vector_store/
│   ├── faiss_index.bin      # Indice vetorial gerado pelo indexer
│   └── metadata.json        # Metadados dos documentos indexados
├── run_indexer.py           # Script para gerar e salvar o indice
├── run_cli_busca.py         # CLI interativa de busca semantica
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

3. Gere o indice vetorial (baixa o dataset e persiste o FAISS em `vector_store/`):

   ```bash
   python run_indexer.py
   ```

   Na primeira execucao o modelo `all-MiniLM-L6-v2` sera baixado automaticamente pelo `sentence-transformers`.

4. Execute a busca semantica interativa:

   ```bash
   python run_cli_busca.py
   ```

   Digite qualquer consulta em ingles e o sistema retornara os artigos mais proximos semanticamente. Para encerrar, digite `sair`, `exit` ou `quit`.

## Dependencias

| Pacote                | Funcao                                      |
|-----------------------|---------------------------------------------|
| `sentence-transformers` | Geracao de embeddings com modelos pre-treinados |
| `faiss-cpu`           | Armazenamento e busca vetorial eficiente    |
| `numpy`               | Manipulacao de arrays de embeddings         |
| `datasets`            | Acesso ao dataset publico no Hugging Face   |
| `python-dotenv`       | Carregamento de variaveis de ambiente       |

## Observacoes

- O dataset `fancyzhx/ag_news` e carregado diretamente do Hugging Face; requer conexao com a internet na primeira execucao.
- O indice FAISS usa distancia L2 (`IndexFlatL2`). Scores menores indicam maior similaridade.
- O limite padrao de indexacao e 150 artigos, configuravel em `app/config.py`.
