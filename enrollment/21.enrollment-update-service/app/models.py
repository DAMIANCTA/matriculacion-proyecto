from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(String, default="active")
    enrollment_date = Column(DateTime(timezone=True), server_default=func.now())

class EnrollmentLog(Base):
    __tablename__ = "enrollment_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enrollment_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True))
    section_id = Column(UUID(as_uuid=True))
    action = Column(String, default="UPDATED")
    timestamp = Column(DateTime, default=func.now())
    source_ip = Column(String)
    details = Column(String)