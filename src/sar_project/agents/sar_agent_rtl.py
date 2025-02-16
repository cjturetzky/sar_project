from sar_project.agents.base_agent import SARBaseAgent
class RTLAgent(SARBaseAgent):
    def __init__(self, name="Rescue Team Leader Agent"):
        super().__init__(
            name=name,
            role="Rescue Team Leader",
            system_message="""You are a Rescue Team Leader for Search and Rescue opertaions. Your role consists of the following duties:
            1. Coordinate Rescue Team members in the field
            2. Facilitate communications between field members and home base
            3. Lead field members in technical operations"""
        )
        self.team_members = {}
        self.current_operation_status = {}
        self.team_status = {}