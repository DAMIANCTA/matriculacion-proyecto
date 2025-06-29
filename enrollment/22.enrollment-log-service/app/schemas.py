from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime


class EnrollmentLogCreate(BaseModel):
    enrollment_id: UUID
    student_id: UUID
    section_id: UUID
    action: str
    source_ip: Optional[str] = None
    details: Optional[str] = None


class EnrollmentLogResponse(EnrollmentLogCreate):
    id: UUID
    timestamp: datetime

    class Config:
        from_attributes = True  
