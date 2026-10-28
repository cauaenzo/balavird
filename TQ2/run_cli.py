from app.services.chatbot_service import gerar_resposta_chatbot

_SAIDA = {"sair", "exit", "quit"}


def main():
    print("-" * 60)
    print("CLI Interativa - Chatbot Python")
    print("Digite sua duvida ou 'sair' para encerrar.")
    print("-" * 60)

    while True:
        try:
            pergunta = input("\nVoce: ").strip()

            if not pergunta:
                continue

            if pergunta.lower() in _SAIDA:
                print("\nEncerrando. Ate mais.")
                break

            print("\nProcessando...")
            resposta = gerar_resposta_chatbot(pergunta)
            print(f"\nAssistente:\n{resposta}")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nInterrompido. Ate mais.")
            break
        except Exception as e:
            print(f"\n[Erro]: {e}")


if __name__ == "__main__":
    main()
