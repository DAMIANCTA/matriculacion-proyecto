from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database, crud

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/history", response_model=schemas.AcademicHistoryResponse)
def create_history(entry: schemas.AcademicHistoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_history_entry(db, entry)
