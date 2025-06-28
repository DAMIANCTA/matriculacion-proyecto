from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud, models, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/enrollments/{enrollment_id}", response_model=schemas.EnrollmentResponse)
def update_enrollment(enrollment_id: str, updated_data: schemas.EnrollmentUpdate, request: Request, db: Session = Depends(get_db)):
    enrollment = crud.update_enrollment(db, enrollment_id, updated_data, request.client.host)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    return enrollment

@app.patch("/enrollments/{enrollment_id}/status", response_model=schemas.EnrollmentResponse)
def update_enrollment_status(enrollment_id: str, status: schemas.StatusUpdate, request: Request, db: Session = Depends(get_db)):
    enrollment = crud.update_enrollment_status(db, enrollment_id, status.status, request.client.host)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    return enrollment