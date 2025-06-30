from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models, schemas, database, crud
from app.services.user_client import verify_user_exists
from app.services.section_client import verify_section_exists
from app.services.enrollment_client import verify_enrollment_exists

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/history", response_model=schemas.AcademicHistoryResponse)
def create_history(entry: schemas.AcademicHistoryCreate, request: Request, db: Session = Depends(get_db)):
    if not verify_user_exists(str(entry.student_id)):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    if not verify_section_exists(str(entry.section_id)):
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    if not verify_enrollment_exists(str(entry.enrollment_id)):
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    return crud.create_history(db=db, entry=entry, source_ip=request.client.host)
