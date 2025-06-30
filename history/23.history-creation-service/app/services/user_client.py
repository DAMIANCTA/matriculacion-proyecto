import requests

def verify_user_exists(user_id: str) -> bool:
    try:
        response = requests.get(f"http://user-reading-service:8081/users/{user_id}")
        return response.status_code == 200
    except Exception:
        return False
