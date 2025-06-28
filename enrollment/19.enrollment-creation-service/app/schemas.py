from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EnrollmentCreate(BaseModel):
    student_id: UUID
    section_id: UUID
    status: str = "activa"

class EnrollmentResponse(EnrollmentCreate):
    id: UUID
    enrollment_date: datetime

class EnrollmentLogCreate(BaseModel):
    student_id: UUID
    section_id: UUID
    action: str
    source_ip: str = None
    details: str = None

class EnrollmentLogResponse(EnrollmentLogCreate):
    id: UUID
    timestamp: datetime