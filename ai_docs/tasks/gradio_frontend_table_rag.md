# AI Task Planning Template

## 1. Task Title
Create a Visually Appealing Gradio Frontend for Table RAG System

## 2. Task Overview
Develop an interactive Gradio web application that provides a user-friendly interface for the existing Table RAG system. The frontend will allow users to query the coffee sales database using natural language, visualize the generated SQL queries, display query results, and present AI-generated answers in an intuitive and visually appealing manner.

## 3. Project Analysis

### Project Context
- **Current State:** The Table RAG system exists as a Python script (`table_rag.py`) with core functionality implemented. The system uses LangChain with Groq (Llama 3.3 70B) to generate SQL queries from natural language questions and answer them using RAG. The backend logic is complete but lacks a user interface.
- **Relevant Codebase:** 
  - `scripts/M07_VectorDB_RAG/table_rag/table_rag.py` - Main RAG implementation with functions: `fetch_information_from_db()`, `create_sql_query()`, and `rag()`
  - `scripts/M07_VectorDB_RAG/table_rag/data_prep.py` - Database creation script
  - SQLite database: `coffee_sales.db` with coffee sales data schema

### Dependencies & Constraints
- **Required Libraries/APIs:** 
  - Gradio (for frontend framework)
  - Existing dependencies: `langchain_groq`, `langchain_core`, `pydantic`, `sqlite3`, `python-dotenv`
  - Optional: `pandas` for better data table formatting
- **Constraints:** 
  - Must maintain compatibility with existing backend functions
  - Database file (`coffee_sales.db`) must be accessible
  - Environment variables (Groq API key) must be properly configured
  - Should handle errors gracefully (SQL errors, API failures, etc.)

## 4. Context & Problem Definition
- **Background:** The Table RAG system demonstrates how to use LLMs to generate SQL queries and answer questions about structured data. Currently, users must modify the Python script directly to ask questions, which is not user-friendly. A Gradio frontend will make this system accessible to non-technical users and provide a better demonstration of the RAG capabilities.
- **The Problem:** Create an intuitive web interface that:
  1. Accepts natural language queries from users
  2. Displays the generated SQL query transparently
  3. Shows the raw database results
  4. Presents the AI-generated answer in a readable format
  5. Provides visual feedback during processing
  6. Handles errors gracefully with user-friendly messages
  7. Includes optional data visualization for query results

## 5. Technical Requirements
- **Platform/Environment:** 
  - Python 3.8+ (compatible with existing dependencies)
  - Gradio 4.0+
  - Existing environment setup with `.env` file for API keys
- **Key Functionality:** 
  1. Text input for user queries
  2. Query execution with loading indicators
  3. Display of generated SQL query (with syntax highlighting if possible)
  4. Display of raw database results in a table format
  5. Display of AI-generated natural language answer
  6. Error handling and user feedback
  7. Optional: Query history/session management
  8. Optional: Basic data visualization (charts for numeric results)
- **Performance:** 
  - Should respond within reasonable time (depends on Groq API latency)
  - Display loading states during API calls
  - Cache table schema information if possible
- **Security:** 
  - Ensure database queries are read-only (SELECT only)
  - Validate user input to prevent SQL injection (though LLM-generated queries should be safe)
  - Keep API keys secure (already handled via .env)

## 6. API & Backend Changes
### New Endpoints
*No new API endpoints required - Gradio will call existing Python functions directly.*

### Database Schema Changes
*No database schema changes required.*

### Logic/Business Rules
- Add input validation for user queries (non-empty, reasonable length)
- Implement SQL query validation to ensure only SELECT statements are executed
- Add error handling wrapper functions for better user experience
- Consider adding query result caching for repeated queries (optional)

## 7. Frontend Changes
- **UI Components:** 
  1. **Header/Title Section:** App title, description, and branding using Gradio's `gr.Markdown()`
  2. **Query Input Section:** `gr.Textbox()` or `gr.TextArea()` for natural language queries
  3. **Action Button:** `gr.Button()` for submitting queries
  4. **Loading Indicator:** Gradio's built-in loading states
  5. **SQL Query Display:** `gr.Code()` component showing generated SQL (with syntax highlighting)
  6. **Results Table:** `gr.Dataframe()` for displaying database results
  7. **Answer Section:** `gr.Markdown()` or `gr.Textbox()` showing AI-generated answer
  8. **Error Display:** Error handling through Gradio's exception handling
  9. **Optional:** `gr.Accordion()` for collapsible sections (query history, app info)
  10. **Optional:** `gr.Plot()` or `gr.BarPlot()` for data visualization

- **User Flow:** 
  1. User opens the Gradio app (via `launch()`)
  2. User sees welcome message and instructions
  3. User enters a natural language question in the input field
  4. User clicks submit button or presses Enter
  5. Loading indicator appears automatically
  6. System generates SQL query (displayed to user)
  7. System executes query and retrieves results (displayed in table)
  8. System generates natural language answer (displayed prominently)
  9. User can ask follow-up questions or modify query

- **State Management:** 
  - Use Gradio's `gr.State()` for:
    - Query history (optional)
    - Previous results (optional)
    - User preferences (optional)
  - Gradio handles state management through its interface components

## 8. Implementation Plan
### Step 1: Planning & Design
1. Sketch UI layout (header, input section, results sections)
2. Design component hierarchy and organization
3. Plan error handling strategy
4. Decide on optional features (visualization, history)
5. Create mockup or wireframe of desired UI
6. Review Gradio component options and best practices

### Step 2: Backend Implementation
1. Create wrapper functions for error handling around existing RAG functions
2. Add input validation functions
3. Add SQL query validation (ensure SELECT-only)
4. Create utility functions for formatting results
5. Add optional caching mechanism for table schema
6. Create a main processing function that Gradio will call

### Step 3: Frontend Implementation
1. Set up Gradio app structure (`gradio_app.py` or `app.py`)
2. Import necessary Gradio components and existing RAG functions
3. Create header section with `gr.Markdown()` for title and description
4. Implement query input component with `gr.Textbox()` or `gr.TextArea()`
5. Add submit button with `gr.Button()`
6. Create output components:
   - `gr.Code()` for SQL query display
   - `gr.Dataframe()` for results table
   - `gr.Markdown()` for AI-generated answer
7. Implement main processing function that connects inputs to outputs
8. Set up error handling using try-except blocks
9. Add optional sidebar or accordion sections for app info
10. Style components using Gradio's theming options
11. Add optional visualization components using `gr.Plot()` or `gr.BarPlot()`
12. Configure Gradio interface with `gr.Interface()` or `gr.Blocks()` for more control

### Step 4: Integration & Testing
1. Test end-to-end flow with various query types
2. Test error scenarios (invalid queries, API failures, database errors)
3. Verify UI responsiveness and loading states
4. Test Gradio app in different modes (local, share link, public URL)
5. Validate that all existing functionality works through the UI
6. Add user instructions/help text
7. Polish visual design using Gradio themes
8. Test with different screen sizes (Gradio responsive design)

## 9. File Structure & Organization
### New Files
- `scripts/M07_VectorDB_RAG/table_rag/gradio_app.py` - Main Gradio application file
- `scripts/M07_VectorDB_RAG/table_rag/utils.py` - Optional utility functions for formatting, validation (if needed)
- `scripts/M07_VectorDB_RAG/table_rag/requirements.txt` - Updated with Gradio dependency (if not already present)

### Modified Files
- Potentially refactor `table_rag.py` to separate UI logic from core RAG logic (optional, for better organization)

### File Organization
```
scripts/M07_VectorDB_RAG/table_rag/
├── table_rag.py          # Existing RAG backend (keep as is)
├── data_prep.py          # Existing data preparation (keep as is)
├── gradio_app.py         # New Gradio frontend
├── utils.py               # Optional utility functions
├── coffee_sales.db       # Database file
└── requirements.txt       # Dependencies
```
