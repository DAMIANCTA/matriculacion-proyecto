import requests

def verify_section_exists(section_id: str) -> bool:
    try:
        response = requests.get(f"http://section-reading-service:3011/sections/{section_id}")
        return response.status_code == 200
    except:
        return False