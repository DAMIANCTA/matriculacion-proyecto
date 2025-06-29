from sqlalchemy.orm import Session
from app import models, schemas

def create_history_entry(db: Session, entry: schemas.AcademicHistoryCreate):
    db_entry = models.AcademicHistory(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
