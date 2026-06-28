MOCK_SLOTS = {
    "cardiology": [
        "Monday 10:00 AM",
        "Monday 2:00 PM",
        "Wednesday 11:30 AM"
    ],
    "dermatology": [
        "Tuesday 9:00 AM",
        "Thursday 1:30 PM"
    ],
    "neurology": [
        "Monday 1:00 PM",
        "Thursday 10:30 AM"
    ],
    "orthopedics": [
        "Wednesday 9:30 AM",
        "Friday 2:30 PM"
    ],
    "general": [
        "Monday 9:00 AM",
        "Tuesday 11:00 AM",
        "Friday 3:00 PM"
    ]
}


def check_available_slots(department="general", date=None):

    if not department:
        department = "general"

    department = department.lower()

    slots = MOCK_SLOTS.get(department, MOCK_SLOTS["general"])

    display_department = department.title()

    if department == "general":
        display_department = "General"

    answer = (
        "I can check for appointment availability.\n\n"
        f"Available {display_department} appointment slots are:"
    )

    return {
        "answer": answer,
        "available_slots": slots
    }