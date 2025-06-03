# CrewAi API

from fastapi import APIRouter, HTTPException, Depends
from .crew_manager import CrewManager, get_crew_manager
from .models import Team, TeamMember
from typing import List

router = APIRouter(
    prefix="/crew",
    tags=["Crew Management"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", response_model=Team, status_code=201)
async def create_new_team(
    team_data: Team,
    manager: CrewManager = Depends(get_crew_manager)
):
    return manager.create_team(team_data)

@router.get("/{team_id}", response_model=Team)
async def get_team_details(
    team_id: str,
    manager: CrewManager = Depends(get_crew_manager)
):
    team = manager.get_team(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.post("/{team_id}/add_member", response_model=TeamMember, status_code=201)
async def add_team_member(
    team_id: str,
    member_data: TeamMember,
    manager: CrewManager = Depends(get_crew_manager)
):
    member = manager.add_member(team_id, member_data)
    if not member:
        raise HTTPException(status_code=404, detail="Team not found")
    return member

@router.get("/", response_model=List[Team])
async def list_all_teams(manager: CrewManager = Depends(get_crew_manager)):
    return manager.get_all_teams()

@router.get("/introspect")
async def crew_introspect(manager: CrewManager = Depends(get_crew_manager)):
    """
    [INTENT:API endpoint for CrewManager introspection]
    [OUTPUT:JSON with team/member stats and last update]
    """
    return manager.introspect()

@router.get("/test")
async def crew_test():
    """
    [INTENT:Quick healthcheck endpoint for CrewAI]
    [OUTPUT:Simple JSON response]
    """
    from datetime import datetime
    return {"status": "ok", "module": "CrewAI", "timestamp": datetime.utcnow().isoformat()}
