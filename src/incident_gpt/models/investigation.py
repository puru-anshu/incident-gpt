import datetime
from uuid import UUID

from pydantic import BaseModel

from incident_gpt.models.enums import InvestigationStatus, Severity


class InvestigationRequest(BaseModel):
    """
    Request model for creating an investigation.
    """
    query: str
    service: str
    environment: str
    severity: Severity
    
class InvestigationResponse(BaseModel):
    """
    Response model for an investigation.
    """
    id: UUID
    created_at: datetime
    status: InvestigationStatus
    request: InvestigationRequest
    

class Investigation(BaseModel):
    """
    Model representing an investigation.
    """
    id: UUID
    created_at: datetime
    status: InvestigationStatus
    request: InvestigationRequest

    