import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import user_client, section_client

# Mock functions to simulate external service responses
def mock_verify_user_exists(user_id: str) -> bool:
    return user_id == "11111111-1111-1111-1111-111111111111"

def mock_verify_section_exists(section_id: str) -> bool:
    return section_id == "22222222-2222-2222-2222-222222222222"

app.dependency_overrides[user_client.verify_user_exists] = mock_verify_user_exists
app.dependency_overrides[section_client.verify_section_exists] = mock_verify_section_exists

client = TestClient(app)

def test_create_enrollment_success():
    payload = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "section_id": "22222222-2222-2222-2222-222222222222",
        "status": "activa"
    }
    response = client.post("/enrollments", json=payload)
    assert response.status_code == 200
    assert response.json()["student_id"] == payload["student_id"]
    assert response.json()["section_id"] == payload["section_id"]

def test_create_enrollment_user_not_found():
    payload = {
        "student_id": "00000000-0000-0000-0000-000000000000",
        "section_id": "22222222-2222-2222-2222-222222222222",
        "status": "activa"
    }
    response = client.post("/enrollments", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Estudiante no encontrado"

def test_create_enrollment_section_not_found():
    payload = {
        "student_id": "11111111-1111-1111-1111-111111111111",
        "section_id": "00000000-0000-0000-0000-000000000000",
        "status": "activa"
    }
    response = client.post("/enrollments", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Sección no encontrada"