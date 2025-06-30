import uuid
from sqlalchemy.orm import Session
from app import models, schemas

def create_history(db: Session, entry: schemas.AcademicHistoryCreate, source_ip: str):
    db_history = models.AcademicHistory(
        id=uuid.uuid4(),
        student_id=entry.student_id,
        section_id=entry.section_id,
        enrollment_id=entry.enrollment_id,
        action=entry.action,
        description=entry.description,
        source_ip=source_ip
    )
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history
