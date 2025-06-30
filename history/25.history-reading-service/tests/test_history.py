from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_by_student():
    response = client.get("/history/by-student/00000000-0000-0000-0000-000000000000")
    assert response.status_code in [200, 404]

def test_get_by_section():
    response = client.get("/history/by-section/00000000-0000-0000-0000-000000000000")
    assert response.status_code in [200, 404]
