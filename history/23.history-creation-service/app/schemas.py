from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class AcademicHistoryCreate(BaseModel):
    student_id: UUID4
    section_id: UUID4
    enrollment_id: UUID4
    action: str
    description: Optional[str] = None

class AcademicHistoryResponse(AcademicHistoryCreate):
    id: UUID4
    recorded_at: datetime

    class Config:
        from_attributes = True
