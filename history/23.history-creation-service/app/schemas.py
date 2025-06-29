from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class AcademicHistoryCreate(BaseModel):
    student_id: UUID
    section_id: UUID
    description: Optional[str] = None

class AcademicHistoryResponse(AcademicHistoryCreate):
    id: UUID
    recorded_at: datetime

    class Config:
        orm_mode = True
