from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
from datetime import datetime

class AcademicHistory(Base):
    __tablename__ = "academic_history"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    description = Column(String, nullable=True)
    recorded_at = Column(DateTime, default=datetime.utcnow)
