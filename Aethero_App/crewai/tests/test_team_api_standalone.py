# AETH-TASK-007 :: ROLE: Lucius :: GOAL: Standalone Pytest tests for CrewAi API endpoints (no external imports)
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from Aethero_App.crewai.team_api import router as crew_router

# Vytvoríme samostatnú FastAPI app len s CrewAi routerom
app = FastAPI()
app.include_router(crew_router)
client = TestClient(app)

def test_create_team():
    response = client.post(
        "/crew/create",
        json={"name": "Alpha Team", "description": "Pioneering new frontiers", "goal": "Achieve singularity"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alpha Team"
    assert data["description"] == "Pioneering new frontiers"
    assert "id" in data
    assert "members" in data
    assert len(data["members"]) == 0

def test_get_team_success():
    response = client.post(
        "/crew/create",
        json={"name": "Alpha Team", "description": "Pioneering new frontiers", "goal": "Achieve singularity"}
    )
    team_id = response.json()["id"]
    response = client.get(f"/crew/{team_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Alpha Team"

def test_get_team_not_found():
    response = client.get("/crew/non-existent-id-123")
    assert response.status_code == 404

def test_add_member_to_team_success():
    response = client.post(
        "/crew/create",
        json={"name": "Alpha Team", "description": "Pioneering new frontiers", "goal": "Achieve singularity"}
    )
    team_id = response.json()["id"]
    member_payload = {"name": "Lucius Prime", "role": "Lead Developer"}
    response = client.post(f"/crew/{team_id}/add_member", json=member_payload)
    assert response.status_code == 201
    member_data = response.json()
    assert member_data["name"] == "Lucius Prime"
    assert member_data["role"] == "Lead Developer"
    assert "id" in member_data
    team_response = client.get(f"/crew/{team_id}")
    team_data = team_response.json()
    assert len(team_data["members"]) == 1
    assert team_data["members"][0]["name"] == "Lucius Prime"

def test_add_member_to_non_existent_team():
    member_payload = {"name": "Ghost Member", "role": "Spectator"}
    response = client.post("/crew/non-existent-id-456/add_member", json=member_payload)
    assert response.status_code == 404

def test_list_teams():
    client.post("/crew/create", json={"name": "Team X", "description": "X factor"})
    client.post("/crew/create", json={"name": "Team Y", "description": "Why factor"})
    response = client.get("/crew/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    team_names = [team["name"] for team in data]
    assert "Team X" in team_names
    assert "Team Y" in team_names
