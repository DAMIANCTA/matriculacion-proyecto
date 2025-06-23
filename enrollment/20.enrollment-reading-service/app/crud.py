from app.models import Enrollment, EnrollmentLog
from app.database import SessionLocal


def get_all_enrollments():
    db = SessionLocal()
    result = db.query(Enrollment).all()
    db.close()
    return result

def get_all_enrollment_logs():
    db = SessionLocal()
    result = db.query(EnrollmentLog).all()
    db.close()
    return result