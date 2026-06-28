from app.rag.retriever import retrieve_documents
from app.rag.rag_pipeline import ask_rag

question = "What is chemotherapy?"

print("=" * 80)
print("QUESTION")
print(question)

# Retrieve documents directly
documents, scores = retrieve_documents(question)

print("=" * 80)
print(f"RETRIEVED CHUNKS: {len(documents)}")
print("=" * 80)

for i, (doc, score) in enumerate(zip(documents, scores), start=1):
    print(f"\n========== CHUNK {i} ==========")
    print(f"Similarity Score: {score:.4f}")
    print(f"Source: {doc.metadata.get('source')}")
    print("-" * 80)
    print(doc.page_content)
    print("-" * 80)

print("\n")

# Now run the full RAG pipeline
response = ask_rag(question)

print("=" * 80)
print("ANSWER")
print("=" * 80)
print(response["answer"])

print("\n" + "=" * 80)
print("SOURCES")
print("=" * 80)

for source in response["sources"]:
    print(f"Document : {source['document']}")
    print(f"Chunk    : {source['chunk']}")
    print("-" * 80)

print("Confidence:", response["confidence"])