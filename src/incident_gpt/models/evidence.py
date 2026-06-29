from pydantic import BaseModel
from  datetime import datetime
from uuid import UUID
from incident_gpt.models.enums import InvestigationStatus, Severity

class Evidence(BaseModel):
    """
    Represents a piece of evidence related to an incident.
    """
    source: str
    title: str
    content: str
    confidence: float
    timestamp: datetime
