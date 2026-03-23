# AI PDF Assistant

An AI-powered application that allows users to upload a PDF and ask questions about its content. The system uses Retrieval Augmented Generation (RAG) to provide accurate, context-based answers.

---

## Project Overview

This project demonstrates how to build an AI application that can read and understand documents. Instead of relying only on a language model's internal knowledge, the system retrieves relevant information from the uploaded PDF and uses it to generate answers.

The application processes the PDF, splits it into smaller text chunks, stores them in a vector database, and retrieves the most relevant parts when a user asks a question.

---

## Features

- Upload and process PDF documents
- Extract text from PDF files
- Split text into manageable chunks
- Store chunks in a vector database (Chroma)
- Perform semantic search using embeddings
- Generate answers using OpenAI's language model
- Display retrieved context for transparency

---

## Tech Stack

- Python
- OpenAI API (LLM)
- ChromaDB (Vector Database)
- PyPDF (PDF text extraction)
- Streamlit (Frontend UI)
- Python-dotenv (Environment variables)

---

## How It Works (Architecture)

The application follows a Retrieval Augmented Generation (RAG) pipeline:

1. The user uploads a PDF file.
2. The system extracts text from the PDF.
3. The text is split into smaller chunks.
4. Each chunk is stored in a vector database (Chroma) as embeddings.
5. When a user asks a question:
   - The question is converted into an embedding.
   - The vector database is searched for the most relevant chunks.
6. The retrieved chunks are sent as context to the language model.
7. The model generates an answer based on the provided context.

```markdown
### Pipeline Overview


PDF → Text → Chunks → Embeddings → Vector Database
↓
User Question
↓
Semantic Search
↓
Relevant Chunks
↓
LLM (OpenAI API)
↓
Answer


---

## Project Structure


ai-pdf-assistant/
│
├── app.py # Streamlit UI (entry point)
├── README.md # Project documentation
├── requirements.txt # Project dependencies
├── .env # API key (not committed)
│
└── src/
├── pdf_reader.py # Extracts text from PDF
├── chunker.py # Splits text into chunks
├── vector_store.py # Handles Chroma vector database
└── rag_pipeline.py # Connects retrieval + LLM

```

### File Responsibilities

- **app.py**  
  Handles user interaction (upload PDF, ask questions, display answers).

- **pdf_reader.py**  
  Extracts raw text from PDF files using PyPDF.

- **chunker.py**  
  Splits large text into smaller overlapping chunks.

- **vector_store.py**  
  Stores chunks as embeddings in Chroma and performs similarity search.

- **rag_pipeline.py**  
  Combines retrieved chunks with the user query and generates answers using the OpenAI API.

---

## How to Run

### 1. Clone the repository


git clone https://github.com/your-username/ai-pdf-assistant.git

cd ai-pdf-assistant


### 2. Create and activate a virtual environment

Windows:


python -m venv .venv
..venv\Scripts\Activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Add your OpenAI API key

Create a `.env` file in the root directory and add:


OPENAI_API_KEY=your_api_key_here


### 5. Run the app


streamlit run app.py


---

## Example Usage

1. Upload a PDF document (e.g., a technical report or article).
2. Wait for the document to be processed.
3. Ask a question such as:
   - "What is a CubeSat?"
   - "What documents are required for flight certification?"
4. The system will:
   - Retrieve relevant parts of the document
   - Generate an answer based on those parts
   - Display both the answer and the retrieved context

---
