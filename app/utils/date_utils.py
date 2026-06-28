def normalize_date(date: str | None) -> str | None:
    """
    Convert natural language dates into weekday names
    supported by the mock appointment tool.
    """

    if not date:
        return None

    date = date.lower()

    weekdays = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    for day in weekdays:
        if day in date:
            return day

    return None