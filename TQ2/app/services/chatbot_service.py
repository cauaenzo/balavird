import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv(
    "OPENAI_BASE_URL",
    "https://api.openai.com/v1",
)
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

if not api_key:
    raise RuntimeError(
        "A variável OPENAI_API_KEY não foi configurada."
    )

# Inicializa os componentes uma única vez.
llm = ChatOpenAI(
    model=model_name,
    temperature=0.7,
    api_key=api_key,
    base_url=base_url,
    timeout=30,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        (
            "Você é um assistente especialista em programação Python. "
            "Responda em português com explicações claras e precisas. "
            "Quando relevante, apresente exemplos de código executáveis, "
            "explique decisões técnicas e destaque possíveis limitações. "
            "Se não souber algo, deixe isso claro."
        ),
    ),
    ("human", "{pergunta}"),
])

chain = prompt | llm | StrOutputParser()


def gerar_resposta_chatbot(pergunta: str) -> str:
    if not pergunta or not pergunta.strip():
        raise ValueError("A pergunta não pode estar vazia.")

    return chain.invoke({"pergunta": pergunta.strip()})
