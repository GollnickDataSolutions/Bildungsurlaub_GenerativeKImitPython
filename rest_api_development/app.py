#%% Packages
from fastapi import FastAPI
from pydantic import BaseModel

#%% ChatRequest
class ChatRequest(BaseModel):
    prompt: str
    context_info: str

#%% App
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/chat")
def chat(request: ChatRequest):
    prompt = request.prompt
    context_info = request.context_info
    
    return {"message": "Hello, World!"}

#%% Run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)