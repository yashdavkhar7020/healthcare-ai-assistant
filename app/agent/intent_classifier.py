import json

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.llm.llm import get_llm
from app.models.router_models import IntentClassification


prompt = PromptTemplate.from_template("""
You are an intelligent routing assistant for a healthcare AI system.

Your ONLY task is to classify the user's request into ONE of the following intents.

--------------------------------------------

INTENT: APPOINTMENT

Choose APPOINTMENT if the user wants to:

- Book an appointment
- Schedule an appointment
- Cancel an appointment
- Reschedule an appointment
- Check doctor availability
- Visit a doctor
- Consult a specialist
- See a physician
- Meet a doctor
- See an oncologist

Extract the department whenever possible.

Supported departments:

- cardiology
- dermatology
- neurology
- orthopedics
- general

Examples:

heart doctor -> cardiology
cardiac doctor -> cardiology
skin specialist -> dermatology
brain doctor -> neurology
bone doctor -> orthopedics
family doctor -> general
general physician -> general
oncologist appointment -> general

--------------------------------------------

INTENT: DOCUMENT

Choose DOCUMENT if the user is asking about information contained in the healthcare documents, including:

- telehealth
- medication refill
- discharge instructions
- insurance
- privacy
- HIPAA
- hospital policies
- healthcare guidelines
- cancer
- oncology
- chemotherapy
- radiation therapy
- immunotherapy
- cancer screening
- cancer diagnosis
- cancer treatment
- tumors

Examples:

What is cancer? -> DOCUMENT
Explain chemotherapy -> DOCUMENT
Tell me about telehealth -> DOCUMENT
What is insurance coverage? -> DOCUMENT

--------------------------------------------

Return ONLY valid JSON.

Example 1

{{
    "intent": "APPOINTMENT",
    "department": "cardiology"
}}

Example 2

{{
    "intent": "APPOINTMENT",
    "department": "general"
}}

Example 3

{{
    "intent": "DOCUMENT",
    "department": null
}}

Rules:

- Return JSON only.
- Do not explain anything.
- Do not use markdown.
- Do not return a schema.
- Department must be null for DOCUMENT.

Question:

{question}
""")

chain = prompt | get_llm(json_mode=True) | StrOutputParser()


def classify_question(question: str) -> IntentClassification:

    raw_output = chain.invoke(
        {
            "question": question
        }
    )

    try:
        data = json.loads(raw_output)

    except Exception:
        data = {
            "intent": "DOCUMENT",
            "department": None
        }

    intent = str(
        data.get("intent", "DOCUMENT")
    ).upper()

    department = data.get("department")

    question_lower = question.lower()

    # Force DOCUMENT for healthcare knowledge queries
    document_keywords = [
        "cancer",
        "chemotherapy",
        "oncology",
        "tumor",
        "tumour",
        "radiation",
        "immunotherapy",
        "telehealth",
        "insurance",
        "privacy",
        "hipaa",
        "discharge",
        "medication refill",
        "guideline",
        "policy",
    ]

    appointment_keywords = [
        "appointment",
        "book",
        "schedule",
        "cancel",
        "reschedule",
        "doctor",
        "physician",
        "specialist",
        "consult",
        "visit",
        "availability",
    ]

    if (
        any(word in question_lower for word in document_keywords)
        and not any(word in question_lower for word in appointment_keywords)
    ):
        intent = "DOCUMENT"
        department = None

    specialties = {
        "cardiology": ["cardiology", "cardiologist", "heart"],
        "dermatology": ["dermatology", "dermatologist", "skin"],
        "neurology": ["neurology", "neurologist", "brain"],
        "orthopedics": ["orthopedic", "orthopedics", "bone"],
    }

    detected_department = None

    for dept, keywords in specialties.items():
        if any(word in question_lower for word in keywords):
            detected_department = dept
            break

    if intent == "APPOINTMENT":
        department = detected_department or "general"
    else:
        department = None

    return IntentClassification(
        intent=intent,
        department=department,
        date=data.get("date")
    )