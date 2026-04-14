#%% Pakete
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
load_dotenv()
from pprint import pprint
from rich.console import Console
from rich.markdown import Markdown
console = Console()

# %% Testen, ob API Key erreichbar ist
os.getenv("GROQ_API_KEY")

#%%
model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key="doris hier bitte den API key reinkopieren",
    temperature=0.4,
    model_kwargs={"top_p":0.9}
)
# %%
res = model.invoke("Tragen alle Mexikaner einen Hut? Ausgabe als Markdown")
# %% schöne Ausgabe (Variante 1)
pprint(res.content, width=50)

#%% noch schönere Ausgabe (Variante 2)
console.print(Markdown(res.content))
# %%
res.model_dump()

#%%
console.print(res.additional_kwargs["reasoning_content"])