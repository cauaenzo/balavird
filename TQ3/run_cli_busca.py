from app.search_service import buscar

_SAIDA = {"sair", "exit", "quit"}


def main():
    print("-" * 60)
    print("Sistema de Busca Semantica - TQ3 (FAISS + Embeddings)")
    print("Digite sua consulta ou 'sair' para encerrar.")
    print("-" * 60)

    while True:
        try:
            consulta = input("\nConsulta: ").strip()

            if not consulta:
                continue

            if consulta.lower() in _SAIDA:
                print("\nEncerrando. Ate mais.")
                break

            resultados = buscar(consulta, k=2)

            if not resultados:
                print("Nenhum resultado encontrado.")
                continue

            print(f"\nResultados para: '{consulta}'")
            print("-" * 60)
            for i, r in enumerate(resultados, start=1):
                print(f"[{i}] ID: {r['id']} | Score (L2): {r['score']:.4f}")
                print(f"Titulo: {r['titulo']}")
                print(f"Conteudo: {r['conteudo']}")
                print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nInterrompido. Ate mais.")
            break
        except FileNotFoundError as e:
            print(f"\n[Erro]: {e}")
            break
        except Exception as e:
            print(f"\n[Erro inesperado]: {e}")


if __name__ == "__main__":
    main()
