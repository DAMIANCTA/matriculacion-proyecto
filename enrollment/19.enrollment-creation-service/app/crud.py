from .models import Enrollment, EnrollmentLog
from sqlalchemy.orm import Session
from .schemas import EnrollmentCreate
from uuid import uuid4
from datetime import datetime


def create_enrollment(db: Session, enrollment: EnrollmentCreate, ip: str):
    db_enrollment = Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.flush()  # importante para obtener el id

    log = EnrollmentLog(
        enrollment_id=db_enrollment.id,
        student_id=db_enrollment.student_id,
        section_id=db_enrollment.section_id,
        action="CREATED",
        timestamp=datetime.utcnow(),
        source_ip=ip,
        details="Matrícula registrada"
    )
    db.add(log)

    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment
