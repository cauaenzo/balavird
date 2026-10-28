from app.embedding_service import indexar


def main():
    print("-" * 60)
    print("Iniciando indexacao via Hugging Face Datasets (TQ3)")
    print("-" * 60)

    try:
        total = indexar()
        print(f"\n{total} documentos indexados com sucesso.")
        print("Arquivos salvos em 'vector_store/'.")
    except Exception as e:
        print(f"\n[Erro na indexacao]: {e}")
        raise


if __name__ == "__main__":
    main()
