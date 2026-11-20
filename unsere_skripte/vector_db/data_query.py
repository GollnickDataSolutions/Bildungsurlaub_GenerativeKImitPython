#%% Pakete
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openrouter import ChatOpenRouter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
import os
from rich.console import Console
from rich.markdown import Markdown
console = Console()
load_dotenv()
#%% Verbindung zur Vektor-DB
EMB_MODEL = "mongodb/voyage-multimodal-3.5"
embeddings = OpenAIEmbeddings(
    model=EMB_MODEL, 
    base_url="https://openrouter.ai/api/v1", 
    api_key=os.getenv("OPENROUTER_API_KEY"),
    check_embedding_ctx_length=False)
vector_db = FAISS.load_local(
    "bedienungsanleitungen", 
    embeddings=embeddings, 
    allow_dangerous_deserialization=True)

# %% 1. Retrieval
def rag(prompt: str = "Mein Router blinkt. was ist das"):
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})

    res = retriever.invoke(prompt)
    # for r in res:
    #     print(r.page_content)
    #     print("-"*20)

    # 2. Augmentation
    # res: [Document(..., page_content=...), Document(..., page_content=...)]

    # Zwischenergebnis: ["page_content1", "page_content2", ...]
    res_list_str = [r.page_content for r in res]

    # Ziel: "page_content1; page_content2; ..., page_contentN"
    context = "; ".join(res_list_str)

    # Prompt Template
    messages = [
        ("system", """
            Du bist ein fachlicher Berater, der sich mit Bedienungsanleitungen auskennt.
            Der Nutzer übergibt dir eine Anfrage und du beantwortest diese auf Basis der Kontextinformationen.
            Beantworte ausschließlich auf Basis des bereitgestellten Kontextes.
            Wenn du die Antwort nicht weißt, sag: 'Ich weiß es nicht'.
            Antworte kurz und präzise (analog zu ASD-STE100).
        """),
        ("user", "Anfrage: {prompt}, Kontextinformationen: {context_info}")
    ]
    prompt_template = ChatPromptTemplate.from_messages(messages)

    # LLM Instanz
    MODEL_NAME = "deepseek/deepseek-v4.1-flash-1017"
    model = ChatOpenRouter(model=MODEL_NAME)

    # Kette erstellen
    chain = prompt_template | model

    # Chain aufrufen
    model_answer = chain.invoke(
        {'prompt': prompt,
        'context_info': context})

    # Antwort überprüfen
    return model_answer.content

#%% Aufruf der Funktion rag(prompt)
console.print(Markdown(rag(prompt="Was ist eine Wallbox")))
#%%
