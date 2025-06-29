from sqlalchemy.orm import Session
from app import models, schemas

def create_log(db: Session, log: schemas.EnrollmentLogCreate):
    db_log = models.EnrollmentLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_all_logs(db: Session):
    return db.query(models.EnrollmentLog).order_by(models.EnrollmentLog.timestamp.desc()).all()

