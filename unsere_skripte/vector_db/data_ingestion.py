#%% Pakete
import os
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

DATA_DIR = Path("data")
INDEX_DIR = "bedienungsanleitungen"

#%% Embeddings
EMB_MODEL = "mongodb/voyage-multimodal-3.5"
embeddings = OpenAIEmbeddings(
    model=EMB_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    check_embedding_ctx_length=False)

#%% Vorhandenen Index laden (falls vorhanden) und bereits verarbeitete Dateien ermitteln
vector_store = None
known_files = set()
if Path(INDEX_DIR, "index.faiss").exists():
    vector_store = FAISS.load_local(
        INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
    for doc in vector_store.docstore._dict.values():
        src = doc.metadata.get("source") or doc.metadata.get("file_path")
        if src:
            known_files.add(Path(src).name)
print(f"Bereits im Index: {len(known_files)} Dateien")

#%% Nur neue PDF-Dateien aus dem Ordner laden
new_files = [f for f in sorted(DATA_DIR.glob("*.pdf")) if f.name not in known_files]
print(f"Neue Dateien: {[f.name for f in new_files]}")

docs = []
for f in new_files:
    docs.extend(PyMuPDF4LLMLoader(file_path=str(f), mode="single").load())
print(len(docs))

#%% Data Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=1000)
docs_splitted = splitter.split_documents(docs)
print(len(docs_splitted))

#%% Embeddings für die neuen Chunks (in Batches) und Speichern
if not docs_splitted:
    print("Keine neuen Dokumente – Index bleibt unverändert.")
else:
    docs_splitted_str = [d.page_content for d in docs_splitted]
    BATCH_SIZE = 5
    docs_embeddings = []
    for i in range(0, len(docs_splitted_str), BATCH_SIZE):
        batch = docs_splitted_str[i:i + BATCH_SIZE]
        docs_embeddings.extend(embeddings.embed_documents(batch))
        print(f"{min(i + BATCH_SIZE, len(docs_splitted_str))}/{len(docs_splitted_str)} Chunks eingebettet")

    text_embeddings = list(zip(docs_splitted_str, docs_embeddings))
    metadatas = [d.metadata for d in docs_splitted]
    if vector_store is None:
        vector_store = FAISS.from_embeddings(
            text_embeddings=text_embeddings, embedding=embeddings, metadatas=metadatas)
    else:
        vector_store.add_embeddings(text_embeddings=text_embeddings, metadatas=metadatas)
    vector_store.save_local(INDEX_DIR)
    print(f"Index gespeichert: {len(new_files)} neue Dateien hinzugefügt")

#%% Test: Ähnlichkeitssuche
# vector_store.similarity_search("Router Fehlermeldung", k=3)
