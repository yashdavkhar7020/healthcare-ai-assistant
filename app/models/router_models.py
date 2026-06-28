from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Intent(str, Enum):
    APPOINTMENT = "APPOINTMENT"
    DOCUMENT = "DOCUMENT"


class IntentClassification(BaseModel):

    intent: Intent

    department: Optional[str] = None

