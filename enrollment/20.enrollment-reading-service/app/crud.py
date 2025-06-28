from sqlalchemy.orm import Session
from .models import Enrollment

def get_all_enrollments(db: Session):
    return db.query(Enrollment).all()

def get_enrollments_by_student(db: Session, student_id: str):
    return db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

def get_enrollments_by_state(db: Session, state: str):
    return db.query(Enrollment).filter(Enrollment.status.ilike(state)).all()
