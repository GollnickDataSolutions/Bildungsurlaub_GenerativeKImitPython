#%% pakete
import os
import truststore
truststore.inject_into_ssl()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()


#%% Modellinstanz erstellen
model = ChatOpenAI(
    model="gpt-4o-mini",
    # api_key=os.getenv("GROQ_API_KEY")  # muss nicht explizit übergeben werden, wenn der Name exakt so lautet
)

#%% Tool für Websuche
search_tool = TavilySearch(
    max_results=4,
    include_domains=["wikipedia.org", "zeit.de", "spiegel.de"]  # Beispielhafte Domains, passe nach Wunsch an
)

#%%
search_tool.invoke("Was ist im Bereich KI zuletzt passiert?")


#%% eigenes Tool zum Zählen von Buchstaben in Wörtern
@tool
def count_letters(word: str, letter: str) -> int:
    """ counts the number of a specific letter in a word
    Args:
        word: The word to count the letters in
        letter: The letter to count
    Returns:
        The number of the letter in the word
    Example:
        count_letters("erdbeere", "e") returns 4
    """
    return word.count(letter)
import datetime
@tool
def get_current_date() -> str:
    """ returns the current date
    Returns:
        The current date
    Example:
        get_current_date() returns "2026-05-22"
    """
    return datetime.datetime.now().strftime("%Y-%m-%d")

#%% Agenten erstellen
agent = create_agent(
    model=model, 
    tools=[search_tool, count_letters, get_current_date],
    system_prompt="""
    Du bist ein hilfreicher Assistent.
    Wenn du eiANTHROPIC_BASE_URLn Tool aufrufst, vertraue immer dem Tool-Ergebnis und gib es exakt so weiter. Überschreibe Tool-Ergebnisse nie mit deinem eigenen Wissen.
    Das aktuelle Datum kannst du mit dem Tool get_current_date() abfragen. Das Ergebnis kannst du dann in deiner Antwort verwenden.
    """
    )
# %% Test
# user_query = "Was ist 2+2?"
# user_query = "Wann ist der deutsche Politiker Helmut Kohl gestorben?"
user_query = "Wieviele 'r' sind im Wort 'strawberry'?"
# user_query = "Was ist gestern im Bereich KI passiert?"
res = agent.invoke({
    "messages": [
        ("user", user_query)
    ]
})

#%% Was liefert das Tool zurück?
for r in res["messages"]:
    if r.type == "tool":
        print(f"Tool: {r.name}, Content: {r.content}")
#%% finale Antwort
res["messages"][-1].content

# %%
res