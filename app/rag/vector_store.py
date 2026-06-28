from functools import lru_cache

from langchain_chroma import Chroma
from app.rag.embeddings import get_embedding_model

VECTOR_DB = "vector_store"


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DB
    )

    return db


@lru_cache(maxsize=1)
def load_vector_store():

    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=VECTOR_DB,
        embedding_function=embedding_model
    )


def add_documents(chunks):

    db = load_vector_store()

    db.add_documents(chunks)

    return db