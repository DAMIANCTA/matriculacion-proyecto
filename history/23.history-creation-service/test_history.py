import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_history_entry():
    payload = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "section_id": "22222222-2222-2222-2222-222222222222",
        "description": "Inscripción a la sección de Matemáticas"
    }
    response = client.post("/history", json=payload)
    assert response.status_code in (200, 201)
    assert "id" in response.json()
