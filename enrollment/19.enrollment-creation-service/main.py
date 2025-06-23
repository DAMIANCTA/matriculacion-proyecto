from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime
from database import SessionLocal, engine, Base
from models import Enrollment, EnrollmentLog

app = FastAPI()

Base.metadata.create_all(bind=engine)

class EnrollmentCreate(BaseModel):
    student_id: str
    section_id: str

@app.post("/enrollments")
def create_enrollment(enrollment: EnrollmentCreate):
    db = SessionLocal()
    try:
        new_enrollment = Enrollment(
            student_id=enrollment.student_id,
            section_id=enrollment.section_id
        )
        db.add(new_enrollment)
        db.commit()
        db.refresh(new_enrollment)

        log = EnrollmentLog(
            enrollment_id=new_enrollment.id,
            student_id=new_enrollment.student_id,
            section_id=new_enrollment.section_id,
            action="CREATED",
            source_ip="127.0.0.1",
            details="Enrollment created"
        )
        db.add(log)
        db.commit()

        return new_enrollment
    finally:
        db.close()
