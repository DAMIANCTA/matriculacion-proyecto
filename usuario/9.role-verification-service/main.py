from fastapi import FastAPI, WebSocket
import asyncpg
import os

app = FastAPI()

@app.websocket("/ws/verify-role")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    conn = await asyncpg.connect(
        user=os.getenv("DB_USER", "damian"),
        password=os.getenv("DB_PASSWORD", "0710"),
        database=os.getenv("DB_NAME", "userdb"),
        host=os.getenv("DB_HOST", "postgres")
    )
    try:
        while True:
            data = await websocket.receive_json()
            username = data.get("username")
            expected_role = data.get("role")

            result = await conn.fetchrow(
                "SELECT role FROM student_users WHERE username = $1", username
            )
            if result and result["role"] == expected_role:
                await websocket.send_json({"status": "ok", "message": "Rol verificado"})
            else:
                await websocket.send_json({"status": "error", "message": "Rol no coincide o usuario no encontrado"})
    except Exception as e:
        await websocket.send_json({"status": "error", "message": str(e)})
    finally:
        await conn.close()