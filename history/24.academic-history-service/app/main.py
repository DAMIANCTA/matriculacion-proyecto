
from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal
from app.services.user_client import verify_user_exists
from app.services.section_client import verify_section_exists
from app.services.enrollment_client import verify_enrollment_exists

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/history", response_model=list[schemas.AcademicHistoryResponse])
def list_all_history(db: Session = Depends(get_db)):
    return crud.get_all_history(db)

@app.get("/history/{history_id}", response_model=schemas.AcademicHistoryResponse)
def get_history_by_id(history_id: str, db: Session = Depends(get_db)):
    return crud.get_history_by_id(db, history_id)

@app.get("/history/student/{student_id}", response_model=list[schemas.AcademicHistoryResponse])
def get_history_by_student(student_id: str, db: Session = Depends(get_db)):
    return crud.get_history_by_student(db, student_id)
