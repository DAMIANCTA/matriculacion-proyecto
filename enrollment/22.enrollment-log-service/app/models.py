from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class EnrollmentLog(Base):
    __tablename__ = "enrollment_logs"

    id = Column(UUID(as_uuid=True), primary_key=True)
    student_id = Column(UUID(as_uuid=True))
    section_id = Column(UUID(as_uuid=True))
    enrollment_id = Column(UUID(as_uuid=True))
    action = Column(String, default="CREATED")
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    source_ip = Column(String)
    details = Column(String)
