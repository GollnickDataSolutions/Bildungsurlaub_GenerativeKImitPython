# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a German educational repository for the course "Generative KI mit Python" (Generative AI with Python). The project demonstrates various AI/ML techniques using Python with a focus on LangChain, different AI providers (Groq, OpenAI, Anthropic, Google GenAI), and practical applications like RAG systems.

## Environment Setup

### Package Management
- Primary package management: **uv** (modern Python package manager)
- Dependencies are specified in `pyproject.toml`
- Sync dependencies with: `uv sync --link-mode copy`
- Alternative: Traditional `pip` with `requirements.txt`

### Virtual Environment
- Use `venv`: `python -m venv .venv`
- Activate on Windows: `.venv\Scripts\activate`
- Activate on Mac/Linux: `source .venv/bin/activate`

### Special Dependencies
- **PyTorch**: Requires manual installation due to Python 3.13 compatibility issues
- Install via: `pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu`

## Project Structure

```
.
├── unsere_skripte/          # Main Python scripts for the course
├── scripts/                # Additional script modules
├── ai_docs/               # AI task documentation and templates
├── slides/                # Presentation materials
├── code/                  # Additional code examples
├── script_bu/             # Backup scripts
├── .env                   # Environment variables (API keys)
├── pyproject.toml         # Project dependencies
├── uv.lock                # uv lock file
├── test_env.py            # Environment test suite
└── README.md              # Basic setup instructions
```

## Key Script Locations

### Main Script Directory: `unsere_skripte/`
Contains core demonstration scripts:
- `chat_groq.py` - Basic Groq chatbot implementation
- `45_semantic_router.py` - Semantic routing with LangChain
- `create_vector_db.py` - Vector database creation
- Various integration scripts with different AI providers

### Table RAG System
Located in `scripts/M07_VectorDB_RAG/table_rag/`:
- `table_rag.py` - Main RAG implementation with Groq (Llama 3.3 70B)
- `data_prep.py` - Database creation
- `coffee_sales.db` - SQLite database with coffee sales data
- Uses Gradio frontend for interactive querying

## Testing

### Environment Testing
- Run environment tests: `python test_env.py`
- Tests API connectivity for OpenAI, Anthropic, Groq
- Verifies `.env` configuration

### Test Structure
- Uses `unittest` framework
- Sequential tests with dependency skipping
- Tests environment variables and API connections

## AI Providers Integration

The project integrates multiple AI providers:
1. **Groq**: Primary provider using `langchain-groq` and `groq` packages
2. **OpenAI**: via `langchain-openai` (pinned to version 1.1.10)
3. **Anthropic**: via `langchain-anthropic`
4. **Google GenAI**: via `google-genai`
5. **Ollama**: via `langchain-ollama` for local models

## Common Development Tasks

### Running Scripts
- Most scripts are Jupyter-style with `#%%` cell markers
- Can be run as regular Python files or in interactive environments
- Scripts use `dotenv` for environment variable loading

### Adding New Dependencies
1. Add to `pyproject.toml` under `dependencies`
2. Run `uv sync --link-mode copy` to update
3. For pip: add to `requirements.txt` and run `pip install -r requirements.txt`

### Environment Configuration
- Copy `.env.example` to `.env` if exists (not in repo)
- Set API keys: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GROQ_API_KEY`
- Always use `load_dotenv()` at script start

## Code Style & Patterns

### LangChain Patterns
- Uses LangChain's expression language (`|` operator)
- Common pattern: `prompt | model | output_parser`
- Imports from `langchain_core`, `langchain_community`, provider-specific packages

### File Organization
- Scripts are self-contained with imports at top
- Use `#%%` markers for cell separation (compatible with VSCode/Jupyter)
- Minimal abstraction - focus on educational clarity

### Error Handling
- Basic try-catch for API calls
- Environment variable validation
- SQL query validation for RAG systems

## Notes for Future Development

- This is an educational repository - prioritize clarity over optimization
- German language in comments and documentation is intentional
- Scripts demonstrate specific concepts - avoid over-engineering
- When modifying RAG systems, maintain the existing function signatures in `table_rag.py`
- The Gradio frontend (`gradio_app.py`) provides interactive UI for the Table RAG system
- Always test environment with `test_env.py` after dependency changes
