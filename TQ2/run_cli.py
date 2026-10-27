import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.chatbot_service import gerar_resposta_chatbot
from dotenv import load_dotenv

load_dotenv()

def main():
    print("=" * 60)
    print("CLI Modo Interativo - Chatbot Python")
    print("Digite sua dúvida de Python ou 'sair' para encerrar.")
    print("=" * 60)

    while True:
        try:
            # Captura o input do usuário pelo terminal
            pergunta_usuario = input("\nVocê: ")
            
            if pergunta_usuario.lower() in ["sair", "exit", "quit"]:
                print("\nEncerrando o chat. Até mais!")
                break
                
            if not pergunta_usuario.strip():
                continue

            print("\nIA pensando...")
            resposta = gerar_resposta_chatbot(pergunta_usuario)
            print(f"\nAssistente:\n{resposta}")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nEncerrando o chat. Até mais!")
            break
        except Exception as e:
            print(f"\n[Erro]: Ocorreu um erro ao processar sua pergunta: {e}")

if __name__ == "__main__":
    main()