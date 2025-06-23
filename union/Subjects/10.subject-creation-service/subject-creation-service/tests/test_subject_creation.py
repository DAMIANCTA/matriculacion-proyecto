import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:3006/ws/create-subject"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            "name": "Física",
            "description": "Dinámica y cinemática",
            "credits": 5,
            "duration": "45 horas"
        }))
        response = await websocket.recv()
        print(response)

asyncio.run(test())
