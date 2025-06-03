# CrewAi Manager

from uuid import uuid4
from .models import Team, TeamMember
from typing import List, Optional

def get_crew_manager():
    return CrewManager.instance()

class CrewManager:
    _instance = None
    def __init__(self):
        self.teams: List[Team] = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = CrewManager()
        return cls._instance

    def create_team(self, team_data) -> Team:
        team_id = str(uuid4())
        new_team = Team(id=team_id, name=team_data.name, description=getattr(team_data, 'description', None), goal=getattr(team_data, 'goal', None), members=[])
        self.teams.append(new_team)
        return new_team

    def add_member(self, team_id: str, member_data) -> Optional[TeamMember]:
        for team in self.teams:
            if team.id == team_id:
                member_id = str(uuid4())
                new_member = TeamMember(id=member_id, name=member_data.name, role=member_data.role)
                team.members.append(new_member)
                return new_member
        return None

    def get_team(self, team_id: str) -> Optional[Team]:
        for team in self.teams:
            if team.id == team_id:
                return team
        return None

    def get_all_teams(self) -> List[Team]:
        return self.teams

    def introspect(self):
        """
        [INTENT:Return crew system introspection]
        [OUTPUT:Dict with team count, member count, last updated timestamp]
        """
        from datetime import datetime
        team_count = len(self.teams)
        member_count = sum(len(team.members) for team in self.teams)
        last_updated = max((getattr(team, 'updated_at', None) for team in self.teams), default=None)
        return {
            "team_count": team_count,
            "member_count": member_count,
            "last_updated": last_updated.isoformat() if last_updated else None,
            "timestamp": datetime.utcnow().isoformat()
        }
