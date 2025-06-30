import requests

def verify_enrollment_exists(enrollment_id: str) -> bool:
    try:
        response = requests.get(f"http://enrollment-reading-service:3020/enrollments/{enrollment_id}")
        return response.status_code == 200
    except:
        return False
