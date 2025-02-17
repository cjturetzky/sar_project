from sar_project.agents.base_agent import SARBaseAgent

class RescuerAgent(SARBaseAgent):

    def __init__(self, name="rescuer"):
        super().__init__(
            name=name,
            role="Rescuer",
            system_message="""You are a rescuer for SAR operations. Your role is:
            1. Conduct field operations to complete missions
            2. Maintain contact with teammates and team leader at all times
            3. Receive messages from team leader"""
        )

    def message(self, message):
        """Dummy function; Really just to make the RTL agent look better."""
        return "Message recieved"