from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class HistoryResponse(BaseModel):
    id: UUID
    student_id: UUID
    section_id: UUID
    enrollment_id: UUID
    action: str
    description: Optional[str]
    source_ip: Optional[str]
    recorded_at: datetime

    class Config:
        orm_mode = True
