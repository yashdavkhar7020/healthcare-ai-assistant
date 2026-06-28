# 🏥 Healthcare AI Assistant

A **Retrieval-Augmented Generation (RAG)** based Healthcare AI Assistant built with **FastAPI**, **LangChain**, **ChromaDB**, and **Meta Llama 3.1 8B Instruct** (via the Hugging Face Inference API).

The application allows users to ingest healthcare documents, build a vector database, and ask natural language questions grounded in the uploaded documents.

---

## 🚀 Features

* 📄 Document ingestion through REST API (`POST /ingest`)
* 🤖 Healthcare question answering using RAG
* 🔍 Semantic search with ChromaDB
* 🧠 Hugging Face sentence-transformer embeddings
* ⚡ FastAPI backend with interactive Swagger documentation
* 🐳 Dockerized application
* ❤️ Health check endpoint
* 📚 Source document references in responses

---

# 🛠️ Tech Stack

| Component            | Technology                                              |
| -------------------- | ------------------------------------------------------- |
| Backend              | FastAPI                                                 |
| API Server           | Uvicorn                                                 |
| Programming Language | Python 3.10                                             |
| LLM                  | Meta Llama 3.1 8B Instruct (Hugging Face Inference API) |
| Framework            | LangChain                                               |
| Embedding Model      | sentence-transformers/all-MiniLM-L6-v2                  |
| Vector Database      | ChromaDB                                                |
| Storage              | SQLite (`chroma.sqlite3`)                               |
| Containerization     | Docker                                                  |
| Testing              | Thunder Client / Swagger UI                             |

---

# 📁 Project Structure

```text
healthcare_ai_assistant/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── data/                  # Healthcare documents
├── scripts/               # Ingestion script
├── vector_store/          # ChromaDB storage
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yashdavkhar7020/healthcare-ai-assistant.git
cd healthcare-ai-assistant
```

---

## 2. Create Virtual Environment

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

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
HF_API_TOKEN=your_huggingface_api_token
```

Replace `your_huggingface_api_token` with your Hugging Face API token.

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 📄 Document Ingestion

Place healthcare documents inside the `data/` directory.

Run the ingestion endpoint:

**POST**

```text
http://localhost:8000/ingest
```

Example response:

```json
{
    "message": "Documents ingested successfully.",
    "documents": 7,
    "chunks": 117
}
```

---

# ❓ Ask Questions

Endpoint:

**POST**

```text
http://localhost:8000/ask
```

Request Body:

```json
{
    "question": "What are the symptoms of diabetes?"
}
```

Example Response:

```json
{
    "answer": "...",
    "sources": [
        "diabetes.pdf"
    ]
}
```

---

# ❤️ Health Check

Endpoint:

```text
GET /health
```

Example Response:

```json
{
    "status": "healthy"
}
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t healthcare-ai-assistant .
```

Run the container:

```bash
docker run -p 8000:8000 healthcare-ai-assistant
```

---

## Using Docker Compose

Start:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

---

# 📌 API Endpoints

| Method | Endpoint  | Description              |
| ------ | --------- | ------------------------ |
| GET    | `/health` | Health check             |
| POST   | `/ingest` | Load and embed documents |
| POST   | `/ask`    | Ask questions using RAG  |

---

# 🧠 RAG Workflow

```text
Documents
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Context
      │
      ▼
Meta Llama 3.1
(Hugging Face API)
      │
      ▼
Final Answer + Sources
```

---

# 📂 Dataset

The application uses healthcare-related PDF and text documents stored in the `data/` directory.

During ingestion:

* Documents are loaded.
* Text is split into chunks.
* Embeddings are generated.
* Chunks are stored in ChromaDB for semantic retrieval.

---

# 🚀 Future Improvements

* Incremental document ingestion
* Authentication for admin endpoints
* Conversation memory
* Streaming LLM responses
* Cloud vector database support
* Background ingestion
* CI/CD pipeline
* Monitoring and logging
* Web dashboard for document uploads

---

# 👨‍💻 Author

**Yash Davkhar**

GitHub:
https://github.com/yashdavkhar7020

---

# 📄 License

This project is developed for educational and assignment purposes.
