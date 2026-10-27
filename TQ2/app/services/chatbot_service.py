import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carrega as variáveis do .env
load_dotenv()


def gerar_resposta_chatbot(pergunta: str) -> str:
  # Inicializa o ChatOpenAI de forma modular.
  # Se o .env tiver a base_url do roteador, ele aponta para lá.
  # Se não tiver, ele usa o padrão da OpenAI oficial.
  llm = ChatOpenAI(
      model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
      temperature=0.7,
      openai_api_key=os.getenv("OPENAI_API_KEY"),
      openai_api_base=os.getenv(
          "OPENAI_BASE_URL", "https://api.openai.com/v1"
      ),
  )

  # Define o prompt estruturado
  prompt = ChatPromptTemplate.from_messages([
      (
          "system",
          (
              "Você é um assistente especialista em programação Python. "
              "Responda às perguntas dos usuários com explicações detalhadas, "
              "claras e exemplos de código quando aplicável."
          ),
      ),
      ("human", "{pergunta}"),
  ])

  # Cria a cadeia (Chain) usando o LCEL do LangChain
  chain = prompt | llm | StrOutputParser()

  # Executa a cadeia
  resposta = chain.invoke({"pergunta": pergunta})
  return resposta