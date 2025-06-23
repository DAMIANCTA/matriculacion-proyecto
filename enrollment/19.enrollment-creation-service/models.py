from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from database import Base

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="ACTIVE")

class EnrollmentLog(Base):
    __tablename__ = "enrollment_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enrollment_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    action = Column(String, default="CREATED")
    timestamp = Column(DateTime, default=datetime.utcnow)
    source_ip = Column(String)
    details = Column(String)
