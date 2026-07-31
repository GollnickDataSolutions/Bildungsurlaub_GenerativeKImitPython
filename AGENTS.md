# AGENTS.md — Generative KI mit Python (Kurs-Repo)

## Setup

```bash
uv sync --link-mode copy
```

PyTorch auf Python 3.13 manuell installieren (keine vollen Wheels):
```bash
pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu
```

`.env` mit API-Keys (OpenAI, Anthropic, etc.) muss im Root liegen — wird via `python-dotenv` geladen.

## Struktur

```
scripts/
  M01_Einführung/        — LLM-Chat, Prompts, Chains, Structured Output
  M03_PretrainedNetworks/ — HuggingFace-Modelle (Summarization, Translation, ZeroShot, FillMask)
  M05_PromptEngineering/  — CoT, Self-Consistency, Self-Critique, Self-Feedback
  M07_VectorDB_RAG/       — DataLoading, Chunking, Embeddings, VectorStore, Retrieval, RAG-Apps
  M09_Agents/             — LangGraph, CrewAI, AG2, OpenAI Agents, MCP
  M10_Deployment/         — Streamlit/Gradio Web-Apps
```

Jede `.py` ist ein eigenständiges Skript — keine Imports unter Skripten hinweg. Direkt ausführen:
```bash
python scripts/M01_Einführung/70_structured_output.py
```

## Wichtige Konventionen

- **Kein Testing, kein Linting, kein CI** — Kurs-Repo, keine Tests vorhanden.
- **Keine Cross-Importe** zwischen Skripten — jedes File ist standalone.
- **`langchain_core.pydantic_v1`** wird verwendet (LangChain-Compat-Schicht), nicht `pydantic` direkt.
- **`unsere_skripte/`** ist im `.gitignore` — persönliche Übungen, nicht Teil des Repos.
- **Slides** liegen als PDFs unter `slides/` (und teilweise `slides/Mxx_*/`).
- **`ai_docs/`** enthält Task-Templates und Feature-Beschreibungen für KI-Aufgaben.
- **`pyproject.toml`** ist die Quelle der Wahrheit für Dependencies (nicht `requirements.txt`).

## Framework-Quirks

- `temperature=0` für deterministische Ausgaben (Structured Output).
- `JsonOutputParser(pydantic_object=...)` für Typ-garantierte LLM-Ausgaben.
- Mehrere LLM-Provider parallel: OpenAI, OpenRouter, Groq, Anthropic, Ollama (lokal).
- Vector Stores: FAISS, Chroma, Qdrant (je nach Modul).
- `langchain_experimental` wird für einige fortgeschrittene Patterns benötigt.

## Ollama (lokal)

```bash
ollama list          # Modelle anzeigen
ollama pull <name>   # Modell herunterladen
```

## Quellen

Alle Referenzen aus den Folien: `Quellen.md`
