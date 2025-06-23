from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import asyncpg
import os

app = FastAPI()

@app.websocket("/ws/create-subject")
async def websocket_create_subject(websocket: WebSocket):
    await websocket.accept()
    conn = await asyncpg.connect(
        user=os.getenv("DB_USER", "damian"),
        password=os.getenv("DB_PASSWORD", "0710"),
        database=os.getenv("DB_NAME", "subjects_db"),
        host=os.getenv("DB_HOST", "postgres")
    )
    try:
        while True:
            data = await websocket.receive_json()
            name = data.get("name")
            description = data.get("description")
            credits = data.get("credits")
            duration = data.get("duration")
            # Asegura que duration sea string
            if duration is not None:
                duration = str(duration)

            await conn.execute(
                "INSERT INTO subjects (id, name, description, credits, duration) VALUES (gen_random_uuid(), $1, $2, $3, $4)",
                name, description, credits, duration
            )
            await websocket.send_json({"status": "ok", "message": "Asignatura creada exitosamente"})
    except Exception as e:
        await websocket.send_json({"status": "error", "message": str(e)})
    finally:
        await conn.close()