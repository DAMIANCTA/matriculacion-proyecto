from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import EnrollmentCreate, EnrollmentResponse
from . import crud
from .services.user_client import verify_user_exists
from .services.section_client import verify_section_exists
import requests  

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/enrollments", response_model=EnrollmentResponse)
def create_enrollment(enrollment: EnrollmentCreate, request: Request, db: Session = Depends(get_db)):
    if not verify_user_exists(str(enrollment.student_id)):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    if not verify_section_exists(str(enrollment.section_id)):
        raise HTTPException(status_code=404, detail="Sección no encontrada")

    created = crud.create_enrollment(db, enrollment, request.client.host)

    log_data = {
        "enrollment_id": str(created.id),
        "student_id": str(created.student_id),
        "section_id": str(created.section_id),
        "action": "CREATED",
        "source_ip": request.client.host,
        "details": "Matrícula registrada desde enrollment-creation-service"
    }
    try:
        requests.post("http://enrollment-log-service:3022/logs", json=log_data)
    except Exception as e:
        print(f"Error al registrar en logs: {e}")

    return created

