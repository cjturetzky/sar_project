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

