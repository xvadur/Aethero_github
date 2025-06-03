import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from fastapi import FastAPI
from fastapi.testclient import TestClient

# Dynamický import podľa existujúceho adresára
try:
    from Aethero_App.crewai.team_api import router as crew_router
except ImportError:
    from aethero_app.crewai.team_api import router as crew_router

def test_list_endpoints():
    app = FastAPI()
    app.include_router(crew_router)
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    print("\n--- AVAILABLE ENDPOINTS ---")
    for path, methods in data["paths"].items():
        print(f"{path}: {list(methods.keys())}")
    print("--------------------------\n")

if __name__ == "__main__":
    test_list_endpoints()
