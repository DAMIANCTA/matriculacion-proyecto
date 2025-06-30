from sqlalchemy.orm import Session
from app import models

def get_by_student(db: Session, student_id: str):
    return db.query(models.AcademicHistory).filter(models.AcademicHistory.student_id == student_id).all()

def get_by_section(db: Session, section_id: str):
    return db.query(models.AcademicHistory).filter(models.AcademicHistory.section_id == section_id).all()
