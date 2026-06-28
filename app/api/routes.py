from fastapi import APIRouter

from app.models.request_models import QuestionRequest
from app.agent.router import route_question
from app.rag.ingest import ingest_documents

router = APIRouter()


@router.post("/ask")
def ask(request: QuestionRequest):
    return route_question(request.question)


@router.post("/ingest")
def ingest():
    result = ingest_documents()

    return {
        "message": "Documents ingested successfully.",
        "documents": result["documents"],
        "chunks": result["chunks"],
    }


@router.get("/health")
def health():
    return {"status": "healthy"}