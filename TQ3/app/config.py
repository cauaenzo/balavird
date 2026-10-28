import os

# Modelo leve e eficiente para embeddings em inglês — bom custo/benefício
MODEL_NAME = "all-MiniLM-L6-v2"

VECTOR_STORE_DIR = "vector_store"
INDEX_PATH = os.path.join(VECTOR_STORE_DIR, "faiss_index.bin")
METADATA_PATH = os.path.join(VECTOR_STORE_DIR, "metadata.json")

# Dataset padrão usado na indexação
DEFAULT_DATASET = "fancyzhx/ag_news"
DEFAULT_SPLIT_LIMIT = 150
