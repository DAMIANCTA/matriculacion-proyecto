from sqlalchemy.orm import Session
from app import models, schemas

def update_enrollment(db: Session, enrollment_id: str, data: schemas.EnrollmentUpdate, ip: str):
    enrollment = db.query(models.Enrollment).filter_by(id=enrollment_id).first()
    if not enrollment:
        return None
    old_status = enrollment.status
    enrollment.status = data.status
    db.commit()
    db.refresh(enrollment)
    log = models.EnrollmentLog(
        enrollment_id=enrollment.id,
        student_id=enrollment.student_id,
        section_id=enrollment.section_id,
        action=f"UPDATED FROM {old_status} TO {data.status}",
        source_ip=ip,
        details="Actualización completa de matrícula"
    )
    db.add(log)
    db.commit()
    return enrollment

def update_enrollment_status(db: Session, enrollment_id: str, status: str, ip: str):
    enrollment = db.query(models.Enrollment).filter_by(id=enrollment_id).first()
    if not enrollment:
        return None
    old_status = enrollment.status
    enrollment.status = status
    db.commit()
    db.refresh(enrollment)
    log = models.EnrollmentLog(
        enrollment_id=enrollment.id,
        student_id=enrollment.student_id,
        section_id=enrollment.section_id,
        action="CANCELADO" if status.lower() == "cancelado" else f"ESTADO CAMBIADO A {status.upper()}",
        source_ip=ip,
        details=f"De {old_status} a {status}"
    )
    db.add(log)
    db.commit()
    return enrollment