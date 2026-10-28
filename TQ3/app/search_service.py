import json
import os

import faiss
import numpy as np

from app.config import INDEX_PATH, METADATA_PATH
from app.embedding_service import get_model


def _carregar_store() -> tuple[faiss.IndexFlatL2, list[dict]]:
    if not os.path.exists(INDEX_PATH) or not os.path.exists(METADATA_PATH):
        raise FileNotFoundError(
            "Vector store nao encontrado. Execute 'run_indexer.py' primeiro."
        )
    index = faiss.read_index(INDEX_PATH)
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        documentos = json.load(f)
    return index, documentos


def buscar(consulta: str, k: int = 2) -> list[dict]:
    """Busca semantica por similaridade vetorial.

    Retorna os k documentos mais proximos do vetor da consulta.
    """
    index, documentos = _carregar_store()

    query_vector = np.array(get_model().encode([consulta])).astype("float32")
    distancias, indices = index.search(query_vector, k)

    resultados = []
    for i, idx in enumerate(indices[0]):
        # idx == -1 indica slot vazio retornado pelo FAISS quando k > total de docs
        if idx == -1 or idx >= len(documentos):
            continue
        doc = documentos[idx]
        resultados.append(
            {
                "id": doc["id"],
                "titulo": doc["titulo"],
                "conteudo": doc["conteudo"],
                "score": float(distancias[0][i]),
            }
        )

    return resultados
