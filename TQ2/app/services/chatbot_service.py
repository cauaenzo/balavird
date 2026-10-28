from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.config import MODEL_NAME, OPENAI_API_KEY, OPENAI_BASE_URL

_llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0.7,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    timeout=30,
    max_retries=2,
)

_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        (
            "Voce e um assistente especialista em programacao Python. "
            "Responda em portugues com explicacoes claras e precisas. "
            "Quando relevante, apresente exemplos de codigo executaveis, "
            "explique decisoes tecnicas e destaque possiveis limitacoes. "
            "Se nao souber algo, deixe isso claro."
        ),
    ),
    ("human", "{pergunta}"),
])

# Chain montada uma vez; reutilizada em todas as requisicoes
_chain = _prompt | _llm | StrOutputParser()


def gerar_resposta_chatbot(pergunta: str) -> str:
    if not pergunta or not pergunta.strip():
        raise ValueError("A pergunta nao pode estar vazia.")
    return _chain.invoke({"pergunta": pergunta.strip()})
