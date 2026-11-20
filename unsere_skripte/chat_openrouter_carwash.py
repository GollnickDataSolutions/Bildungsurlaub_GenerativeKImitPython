#%% Pakete
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate 
import os
from dotenv import load_dotenv
load_dotenv()
# %% Umgebungsvariablen zugreifen
os.getenv("OPENROUTER_API_KEY")

#%% Promptvorlage
messages = [
    ("system", """
        Du bist ein freundlicher Asistent
    """),
    ("user", "Thema: <thema>{topic}</thema>")
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt_template

#%% Auf ein Modell zugreifen
# MODEL_NAME = "deepseek/deepseek-v4.1-flash-1017"
MODEL_NAME = "meta-llama/llama-3.3-70b-instruct"
model = ChatOpenRouter(model=MODEL_NAME)

#%% Kette verbinden
chain = prompt_template | model

# %% Anfrage an die Kette senden
inputs = {
    'topic': 'die autowaschanlage ist 50m entfernt. soll ich laufen oder fahren'
}
res = chain.invoke(inputs)

# %% Was kam vom Modell zurück?
from pprint import pprint
pprint(res.content)

#%% Metadaten anzeigen
res.response_metadata

#%%

