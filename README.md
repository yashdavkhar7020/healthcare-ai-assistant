# Healthcare AI Assistant

## Overview

Healthcare AI Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to ask healthcare-related questions using information retrieved from a custom document collection. The system combines semantic search with a Large Language Model (LLM) to generate accurate, context-aware responses grounded in the uploaded documents.

The project is built using FastAPI, LangChain, ChromaDB, and the Hugging Face Inference API. It also includes a Streamlit interface for interacting with the backend.

---

# Features

* Retrieval-Augmented Generation (RAG) based question answering
* REST APIs built with FastAPI
* Document ingestion through an API endpoint
* Semantic search using ChromaDB
* Hugging Face sentence-transformer embeddings
* Meta Llama 3.1 8B Instruct for response generation
* Source-aware responses
* Dockerized deployment
* Streamlit user interface
* Health monitoring endpoint

---

# Technology Stack

| Component            | Technology                                                  |
| -------------------- | ----------------------------------------------------------- |
| Backend              | FastAPI                                                     |
| Frontend             | Streamlit                                                   |
| Programming Language | Python 3.10                                                 |
| Framework            | LangChain                                                   |
| LLM                  | Meta Llama 3.1 8B Instruct (via Hugging Face Inference API) |
| Embedding Model      | sentence-transformers/all-MiniLM-L6-v2                      |
| Vector Database      | ChromaDB                                                    |
| Vector Storage       | SQLite (`chroma.sqlite3`)                                   |
| API Server           | Uvicorn                                                     |
| Containerization     | Docker                                                      |
| Testing              | Pytest, Thunder Client                                      |

---

# Project Structure

```text
healthcare-ai-assistant/

│
├── app/
│   │
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # Environment variables
│   ├── schemas.py              # Pydantic request/response models
│   │
│   ├── api/
│   │      ask.py               # /ask endpoint
│   │      ingest.py            # /ingest endpoint
│   │      health.py            # /health endpoint
│   │
│   ├── rag/
│   │      loader.py            # Load documents
│   │      splitter.py          # Document chunking
│   │      embeddings.py        # Embedding generation
│   │      vectorstore.py       # ChromaDB operations
│   │      retriever.py         # Similarity search
│   │      prompt.py            # Prompt template
│   │
│   ├── llm/
│   │      ollama_client.py     # LLM interface
│   │
│   ├── agents/
│   │      router.py
│   │      appointment_tool.py
│   │
│   ├── services/
│   │      rag_service.py
│   │      answer_service.py
│   │
│   ├── utils/
│   │      logger.py
│   │      helpers.py
│   │
│   └── tests/
│
├── ui/
│      app.py
│      api_client.py
│
├── data/
│      appointment_policy.txt
│      discharge.txt
│      telehealth.txt
│      insurance.txt
│      medication.txt
│      privacy.txt
│
├── vector_store/
├── logs/
│      app.log
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

----

# Dataset

The application uses healthcare-related text documents stored inside the `data/` directory.

Current dataset includes:

* Appointment Policy
* Discharge Instructions
* Telehealth Guidelines
* Insurance Information
* Medication Information
* Privacy Policy

During ingestion the system:

1. Loads all documents.
2. Splits them into smaller chunks.
3. Generates vector embeddings.
4. Stores the embeddings inside ChromaDB.
5. Makes the knowledge available for semantic retrieval.

New documents can be added simply by placing them inside the `data/` directory and calling the `/ingest` endpoint.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/yashdavkhar7020/healthcare-ai-assistant.git

cd healthcare-ai-assistant
```

## Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Backend

Start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

API documentation:

```
http://localhost:8000/docs
```

---

# Running the Streamlit UI

Open another terminal.

```bash
streamlit run ui/app.py
```

---

# Docker

## Build

```bash
docker build -t healthcare-ai-assistant .
```

## Run

```bash
docker run -p 8000:8000 healthcare-ai-assistant
```

## Using Docker Compose

Start services

```bash
docker compose up --build
```

Run in detached mode

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# API Endpoints

## Health Check

**GET**

```
/health
```

Example response

```json
{
    "status": "healthy"
}
```

---

## Ingest Documents

**POST**

```
/ingest
```

Example response

```json
{
    "message": "Documents ingested successfully.",
    "documents": 6,
    "chunks": 117
}
```

---

## Ask Questions

**POST**

```
/ask
```

Example request

```json
{
    "question": "What is the hospital appointment policy?"
}
```

Example response

```json
{
    "answer": "...",
    "sources": [
        "appointment_policy.txt"
    ]
}
```

---

# System Architecture

```
Healthcare Documents
          │
          ▼
Document Loader
          │
          ▼
Text Splitter
          │
          ▼
Embedding Model
          │
          ▼
ChromaDB Vector Store
          │
          ▼
User Question
          │
          ▼
Similarity Search
          │
          ▼
Relevant Context
          │
          ▼
Meta Llama 3.1
(Hugging Face Inference API)
          │
          ▼
Generated Answer
```

---

# Models Used

### Large Language Model

* Meta Llama 3.1 8B Instruct
* Accessed through the Hugging Face Inference API

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Vector Database

* ChromaDB
* Persistent storage using SQLite

---

# Prompting Strategy

The application follows a Retrieval-Augmented Generation (RAG) workflow.

1. Convert the user query into an embedding.
2. Retrieve the most relevant document chunks from ChromaDB.
3. Construct a prompt containing the retrieved context and user question.
4. Send the prompt to the LLM.
5. Return the generated answer along with document sources.

This approach grounds the LLM's response in the available documents and reduces hallucinations.

---

# Limitations

* Limited to the uploaded healthcare documents.
* Depends on the quality and coverage of the dataset.
* Requires access to the Hugging Face Inference API.
* Does not maintain conversation history.
* No authentication or authorization for API endpoints.
* Local ChromaDB storage is intended for development and small deployments.

---

# Future Improvements

* Incremental document ingestion
* Authentication and authorization
* Conversation memory
* Streaming responses
* Background ingestion
* Cloud-hosted vector database
* Monitoring and logging
* CI/CD pipeline
* Document upload through the web interface
* Support for additional document formats

---

# Author

Yash Davkhar

GitHub: https://github.com/yashdavkhar7020

---

# License

This project was developed for educational and learning purposes.
