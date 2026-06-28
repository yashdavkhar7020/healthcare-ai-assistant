from app.rag.vector_store import load_vector_store


def retrieve_documents(question: str, k: int = 4):
    """
    Retrieve top-k relevant chunks along with similarity scores.
    """

    db = load_vector_store()

    results = db.similarity_search_with_score(
        question,
        k=k
    )

    documents = []
    scores = []

    for doc, score in results:
        documents.append(doc)
        scores.append(score)

    return documents, scores