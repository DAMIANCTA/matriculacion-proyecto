from fastapi import FastAPI
from app import crud, models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/enrollments")
def read_enrollments():
    return crud.get_all_enrollments()

@app.get("/enrollment-logs")
def read_enrollment_logs():
    return crud.get_all_enrollment_logs()
