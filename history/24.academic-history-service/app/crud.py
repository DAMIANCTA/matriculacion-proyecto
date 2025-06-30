
from sqlalchemy.orm import Session
from app import models, schemas
import uuid

def get_all_history(db: Session):
    return db.query(models.AcademicHistory).all()

def get_history_by_id(db: Session, history_id: str):
    return db.query(models.AcademicHistory).filter(models.AcademicHistory.id == history_id).first()

def get_history_by_student(db: Session, student_id: str):
    return db.query(models.AcademicHistory).filter(models.AcademicHistory.student_id == student_id).all()
