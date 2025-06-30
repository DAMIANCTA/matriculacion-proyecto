from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base
import uuid

class AcademicHistory(Base):
    __tablename__ = "academic_history"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    enrollment_id = Column(UUID(as_uuid=True), nullable=False)
    action = Column(String, nullable=False)
    description = Column(String)
    source_ip = Column(String)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
