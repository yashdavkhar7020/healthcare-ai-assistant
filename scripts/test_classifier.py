from app.agent.intent_classifier import classify_question

questions = [
    "Book a heart doctor appointment tomorrow",
    "Need a skin specialist",
    "Can I refill my medication?",
    "Can I visit a neurologist next week?",
    "Can I refill my medication?",
    "Explain discharge instructions",
    "Book an orthopedic consultation",
    "Can I cancel tomorrow's appointment?",
]

for q in questions:

    print("=" * 80)

    print(q)

    result = classify_question(q)

    print(result)

    print(result.intent)

    print(result.department)