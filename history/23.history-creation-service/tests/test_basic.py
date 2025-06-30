from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_history_fail():
    response = client.post("/history", json={
        "student_id": "invalid-uuid",
        "section_id": "invalid-uuid",
        "enrollment_id": "invalid-uuid",
        "action": "MATRICULADO"
    })
    assert response.status_code == 422
