from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store


print("=" * 50)
print("Loading documents...")
docs = load_documents()
print(f"Loaded {len(docs)} documents.")

print("=" * 50)
print("Splitting documents...")
chunks = split_documents(docs)
print(f"Generated {len(chunks)} chunks.")

print("=" * 50)
print("Creating Vector Store...")
create_vector_store(chunks)

print("=" * 50)
print("✅ Vector Store Created Successfully!")