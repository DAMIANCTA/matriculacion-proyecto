from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EnrollmentResponse(BaseModel):
    id: UUID
    student_id: UUID
    section_id: UUID
    status: str
    enrollment_date: datetime

    class Config:
        orm_mode = True
