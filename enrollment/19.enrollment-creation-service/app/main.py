from fastapi import FastAPI, Depends, HTTPException, Request

from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import EnrollmentCreate, EnrollmentResponse
from . import crud
from .services.user_client import verify_user_exists
from .services.section_client import verify_section_exists

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
    
    ip = request.client.host
    return crud.create_enrollment(db, enrollment, ip)  
