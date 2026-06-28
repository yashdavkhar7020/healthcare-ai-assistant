from app.agent.intent_classifier import classify_question
from app.agent.appointment_tool import check_available_slots
from app.rag.rag_pipeline import ask_rag
from app.models.router_models import Intent


def route_question(question: str):

    classification = classify_question(question)

    if classification.intent == Intent.APPOINTMENT:

        department = classification.department or "general"

        return check_available_slots(department)

    return ask_rag(question)