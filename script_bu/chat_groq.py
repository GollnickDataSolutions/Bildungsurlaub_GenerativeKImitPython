#%% Pakete
from langchain_groq.chat_models import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import os

#%% Prüfen, ob der API Key verfügbar ist
os.getenv("GROQ_API_KEY")

#%% Modellinstanz erstellen
MODEL_NAME = "openai/gpt-oss-20b"
model = ChatGroq(
    model_name=MODEL_NAME
    # temperature=0.0,
    # max_retries=2,
    # api_key=os.getenv("GROQ_API_KEY")  # muss nicht explizit angegeben werden, da unser Key exakt der Erwartung von ChatGroq entspricht
    # other params...
)
# %%
