from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/history/by-student/{student_id}", response_model=list[schemas.HistoryResponse])
def get_by_student(student_id: str, db: Session = Depends(get_db)):
    return crud.get_by_student(db, student_id)

@app.get("/history/by-section/{section_id}", response_model=list[schemas.HistoryResponse])
def get_by_section(section_id: str, db: Session = Depends(get_db)):
    return crud.get_by_section(db, section_id)
