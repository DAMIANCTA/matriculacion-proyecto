from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncpg
import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.websocket("/ws/update-subject")
async def update_subject(websocket: WebSocket):
    await websocket.accept()
    conn = await asyncpg.connect(
        user=os.getenv("DB_USER", "damian"),
        password=os.getenv("DB_PASSWORD", "0710"),
        database=os.getenv("DB_NAME", "subjects_db"),
        host=os.getenv("DB_HOST", "subjects_db")
    )
    try:
        while True:
            data = await websocket.receive_json()
            subject_id = data.get("id")
            name = data.get("name")
            description = data.get("description")
            credits = data.get("credits")
            duration = data.get("duration")

            query = """
                UPDATE subjects 
                SET name = $1, description = $2, credits = $3, duration = $4 
                WHERE id = $5
            """
            result = await conn.execute(query, name, description, credits, duration, subject_id)

            await websocket.send_json({
                "status": "ok",
                "message": f"Asignatura actualizada: {result}"
            })
    except WebSocketDisconnect:
        print("WebSocket desconectado")
    except Exception as e:
        try:
            await websocket.send_json({"status": "error", "message": str(e)})
        except:
            pass
    finally:
        await conn.close()