from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enrollment Log Service")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/logs", response_model=schemas.EnrollmentLogResponse)
def create_log(log: schemas.EnrollmentLogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log=log)

@app.get("/logs", response_model=list[schemas.EnrollmentLogResponse])
def get_logs(db: Session = Depends(get_db)):
    logs = crud.get_all_logs(db)
    if not logs:
        raise HTTPException(status_code=404, detail="No se encontraron logs")
    return logs
