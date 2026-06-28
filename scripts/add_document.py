from pathlib import Path

from langchain_core.documents import Document

from app.rag.splitter import split_documents
from app.rag.vector_store import add_documents

FILE = Path("data") / "cancer_care_guidelines.txt"

print("=" * 50)
print("Loading new document...")

text = FILE.read_text(encoding="utf-8")

doc = Document(
    page_content=text,
    metadata={
        "source": FILE.name
    }
)

print("=" * 50)
print("Splitting document...")

chunks = split_documents([doc])

print(f"Generated {len(chunks)} chunks.")

print("=" * 50)
print("Adding to existing Chroma database...")

add_documents(chunks)

print("=" * 50)
print("✅ Document Added Successfully!")