from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.rag.retriever import retrieve_documents
from app.rag.prompt import RAG_PROMPT
from app.llm.llm import get_llm


prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=RAG_PROMPT
)

llm = get_llm()

parser = StrOutputParser()


def ask_rag(question: str):

    documents, scores = retrieve_documents(question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    sources = []

    seen = set()

    for doc in documents:

        source = doc.metadata["source"]

        if source not in seen:

            seen.add(source)

            sources.append(
                {
                    "document": source,
                    "chunk": doc.page_content[:250]
                }
            )

    chain = prompt | llm | parser

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    # ----------------------------------
    # Confidence Calculation
    # ----------------------------------

    best_score = min(scores)

    if best_score < 0.40:
        confidence = "high"

    elif best_score < 0.80:
        confidence = "medium"

    else:
        confidence = "low"

    return {
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }