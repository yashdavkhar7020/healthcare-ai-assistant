from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store


def ingest_documents():

    # Load documents
    documents = load_documents()

    # Split into chunks
    chunks = split_documents(documents)

    # Create vector database
    create_vector_store(chunks)

    return {
        "documents": len(documents),
        "chunks": len(chunks)
    }