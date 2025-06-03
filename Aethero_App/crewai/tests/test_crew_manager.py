# Test CrewManager

import unittest
from ..crew_manager import CrewManager
from ..models import TeamMember

class TestCrewManager(unittest.TestCase):
    def setUp(self):
        self.manager = CrewManager()

    def test_create_team(self):
        team = self.manager.create_team("Team Alpha")
        self.assertEqual(team.name, "Team Alpha")
        self.assertEqual(len(self.manager.teams), 1)

    def test_add_member(self):
        team = self.manager.create_team("Team Beta")
        member = TeamMember(id=1, name="John Doe", role="Developer")
        updated_team = self.manager.add_member(team.id, member)
        self.assertEqual(len(updated_team.members), 1)
        self.assertEqual(updated_team.members[0].name, "John Doe")

    def test_remove_member(self):
        team = self.manager.create_team("Team Gamma")
        member = TeamMember(id=1, name="Jane Doe", role="Designer")
        self.manager.add_member(team.id, member)
        updated_team = self.manager.remove_member(team.id, member.id)
        self.assertEqual(len(updated_team.members), 0)

if __name__ == "__main__":
    unittest.main()
