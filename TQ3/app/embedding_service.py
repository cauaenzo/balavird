import json
import os

import faiss
import numpy as np
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

from app.config import (
    DEFAULT_DATASET,
    DEFAULT_SPLIT_LIMIT,
    INDEX_PATH,
    METADATA_PATH,
    MODEL_NAME,
    VECTOR_STORE_DIR,
)

# Instância compartilhada do modelo — carregada uma vez, reutilizada em todo o processo
_model: SentenceTransformer | None = None


def get_model() -> SentenceTransformer:
    # Lazy loading: evita recarregar o modelo a cada chamada
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def _carregar_dataset(dataset_name: str, split_limit: int) -> list[dict]:
    # Normaliza os campos do dataset para o formato interno do sistema
    dataset = load_dataset(dataset_name, split=f"train[:{split_limit}]")
    return [
        {
            "id": i + 1,
            "titulo": f"Artigo AG News #{i + 1}",
            "conteudo": item.get("text", ""),
        }
        for i, item in enumerate(dataset)
    ]


def _construir_indice_faiss(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


def _persistir(index: faiss.IndexFlatL2, documentos: list[dict]) -> None:
    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(documentos, f, ensure_ascii=False, indent=4)


def indexar(
    dataset_name: str = DEFAULT_DATASET,
    split_limit: int = DEFAULT_SPLIT_LIMIT,
) -> int:
    """Carrega o dataset, gera embeddings e persiste o indice FAISS em disco.

    Retorna o total de documentos indexados.
    """
    print(f"Baixando dataset '{dataset_name}' do Hugging Face...")
    documentos = _carregar_dataset(dataset_name, split_limit)

    textos = [doc["conteudo"] for doc in documentos]

    print("Gerando embeddings...")
    model = get_model()
    embeddings = np.array(model.encode(textos, show_progress_bar=True)).astype("float32")

    index = _construir_indice_faiss(embeddings)
    _persistir(index, documentos)

    return len(documentos)
