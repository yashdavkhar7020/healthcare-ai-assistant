from app.rag.retriever import retrieve_documents

docs = retrieve_documents(
    "Can a patient request medication refill through telehealth?"
)

print("=" * 60)

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("-" * 60)
    print("Source:", doc.metadata["source"])
    print(doc.page_content[:300])