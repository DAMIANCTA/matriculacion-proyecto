from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
import asyncpg
import os

app = FastAPI()
pool = None  # Declarar pool global

@app.on_event("startup")
async def startup():
    global pool
    pool = await asyncpg.create_pool(
        user=os.getenv("DB_USER", "damian"),
        password=os.getenv("DB_PASSWORD", "0710"),
        database=os.getenv("DB_NAME", "subjects_db"),
        host=os.getenv("DB_HOST", "postgres")
    )

@app.websocket("/ws/subjects")
async def subject_websocket(websocket: WebSocket):
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
            if data.get("operation") == "get_all":
                rows = await conn.fetch("SELECT * FROM subjects")
                subjects = []
                for row in rows:
                    subject = dict(row)
                    subject["id"] = str(subject["id"])  # Convertir UUID a string
                    subjects.append(subject)
                await websocket.send_json({"status": "ok", "subjects": subjects})
            else:
                await websocket.send_json({"status": "error", "message": "Operación no válida"})
    except WebSocketDisconnect:
        print("WebSocket desconectado")
    except Exception as e:
        try:
            await websocket.send_json({"status": "error", "message": str(e)})
        except:
            pass
    finally:
        await conn.close()

@app.get("/subjects/{subject_id}")
async def get_subject_by_id(subject_id: str):
    query = "SELECT * FROM subjects WHERE id = $1"
    async with pool.acquire() as connection:
        result = await connection.fetchrow(query, subject_id)
        if result:
            return dict(result)
        else:
            raise HTTPException(status_code=404, detail="Subject not found")