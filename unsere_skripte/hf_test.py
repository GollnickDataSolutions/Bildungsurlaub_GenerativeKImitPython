#%% Pakete
from transformers import pipeline

#%%
classifier = pipeline(task="text-classification", model="ProsusAI/finbert")
classifier("Stocks rallied and the British pound gained.")
# [{'label': 'positive', 'score': 0.898...}]

# %%
