from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/enrollments", response_model=list[schemas.EnrollmentResponse])
def get_all_enrollments(db: Session = Depends(get_db)):
    return crud.get_all_enrollments(db)

@app.get("/enrollments/by-student/{student_id}", response_model=list[schemas.EnrollmentResponse])
def get_enrollments_by_student(student_id: str, db: Session = Depends(get_db)):
    return crud.get_enrollments_by_student(db, student_id)

@app.get("/enrollments/by-state", response_model=list[schemas.EnrollmentResponse])
def get_enrollments_by_state(state: str, db: Session = Depends(get_db)):
    return crud.get_enrollments_by_state(db, state)
