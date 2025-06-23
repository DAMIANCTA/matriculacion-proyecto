from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True))
    section_id = Column(UUID(as_uuid=True))
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="ACTIVE")

class EnrollmentLog(Base):
    __tablename__ = "enrollment_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True))
    action = Column(String)
    section_id = Column(UUID(as_uuid=True))
    timestamp = Column(DateTime, default=datetime.utcnow)
    source_ip = Column(String)
    details = Column(String)