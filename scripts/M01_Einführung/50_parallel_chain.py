
#%% packages
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% Bert's Norton360 Problem
import truststore
truststore.inject_into_ssl()

#%% Model Instance
model = ChatOpenRouter(model="google/gemini-3.5-flash-lite", temperature=0)

#%% Prepare Prompts
# example: style variations (friendly, polite) vs. (savage, angry)
polite_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Reply in a friendly and polite manner. answer in one sentence."),
    ("human", "{topic}")
])

savage_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Reply in a savage and angry manner. answer in one sentence."),
    ("human", "{topic}")
])

#%% Prepare Chains
polite_chain = polite_prompt | model | StrOutputParser()
savage_chain = savage_prompt | model | StrOutputParser()


# %% Runnable Parallel
map_chain = RunnableParallel(
    polite=polite_chain,
    savage=savage_chain
)

# %% Invoke
topic = "Was ist der Sinn des Lebens?"
result = map_chain.invoke({"topic": topic})
# %% Print
from pprint import pprint
pprint(result, width=60)
# %%
