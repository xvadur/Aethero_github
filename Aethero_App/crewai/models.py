# CrewAi Models

from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

class TeamMember(BaseModel):
    id: str = str(uuid4())
    name: str
    role: str
    email: Optional[str] = None

class Team(BaseModel):
    id: str = str(uuid4())
    name: str
    members: List[TeamMember] = []
    description: Optional[str] = None
    goal: Optional[str] = None
