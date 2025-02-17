import pytest
from sar_project.agents.sar_agent_rtl import RTLAgent

class TestRTLAgent:
    @pytest.fixture
    def agent(self):
        return RTLAgent()

    def test_initialization(self, agent):
        assert agent.name == "rtl_agent"
        assert agent.role == "Rescue Team Leader"
        assert agent.mission_status == "standby"

    def test_clear_op(self, agent):
        message = {
            "clear_op":True
        }
        response = agent.process_request(message)
        assert response == "Operation Cleared"
        assert agent.mission_status == "Off-Duty"

    def test_new_op(self, agent):
        message = {
            "new_op":True
        }
        response = agent.process_request(message, members=["CJ", "Franz", "Neeraja"])
        assert response == "Operation Created; Previous Operation Cleared"
        assert agent.mission_status == "Planning Operation"
        assert len(agent.team_members) == 3

    def test_notify_team(self, agent):
        message = ("Lost Hiker: 25 yrs old, female, red hair, wearing green puffer jacket. Nightfall in 1 hour, "
                   "high winds expected.")
        response = agent.notify_team(message)
        print(response.text)
        assert response