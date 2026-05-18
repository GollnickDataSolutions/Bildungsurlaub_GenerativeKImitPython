#%% Pakete
from langchain_openai import ChatOpenAI
from pprint import pprint
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
# %% Testen, ob OPENROUTER_API_KEY verfügbar ist
os.getenv("OPENROUTER_API_KEY")

#%% Modellinstanz erstellen
# model = ChatOpenAI(
#     model="google/gemma-4-26b-a4b-it",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY")
#     )
# # %% Modell aufrufen (invoken)
# res = model.invoke("Was weißt du über 42?")

# # %% Modellergebnisse ansehen
# res.model_dump()

# #%% Modellantwort
# pprint(res.content)

#%% Prompt Template
messages = [
    ("system", """
        Du bist guter Witzeerzähler im Stil von Til Reiners.
        Der Nutzer übergibt dir ein Thema und du erzeugst einen guten Witz.
        Der Witz sollte max. 100 Wörter haben.
    """
    ),
    ("user", "Thema: {thema}")

]
prompt_template = ChatPromptTemplate.from_messages(messages)

#%% Implementierung mit OpenRouter
model = ChatOpenRouter(
    model="google/gemma-4-26b-a4b-it",
    temperature=0.9,
    top_p=0.9,
    max_completion_tokens=300,
    timeout=30000,  # Millisekunden (langchain-openrouter mapt auf timeout_ms)
    )
# res = model.invoke("Was weißt du über 42?")
# %% Chain erstellen
chain = prompt_template | model

#%% Chain aufrufen
user_prompt = "Benzinpreise"
res = chain.invoke({"thema": user_prompt})


pprint(res.content)



# %%
