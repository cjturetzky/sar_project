from sar_project.agents.base_agent import SARBaseAgent


class RTLAgent(SARBaseAgent):

    def __init__(self, name="rtl_agent"):
        super().__init__(
            name=name,
            role="Rescue Team Leader",
            system_message="""You are a Rescue Team Leader for Search and Rescue opertaions. Your role consists of the following duties:
            1. Coordinate Rescue Team members in the field
            2. Facilitate communications between field members and home base
            3. Lead field members in technical operations"""
        )
        self.team_members = []
        self.team_status = {}
        self.op_chief = {}

    def process_request(self, message, status=None, member=None):
        """process Team based requests"""
        try:
            if "get_team_members" in message:
                return self.get_team_members()
            elif "get_op_status" in message:
                return self.get_status()
            elif "get_team_status" in message:
                return self.get_team_status()
            elif "clear_op" in message:
                self.clear_op()
                return "Operation Cleared"
            elif "new_op" in message:
                self.new_op()
                return "Operation Created; Previous Operation Cleared"
            elif "update_team_status" in message:
                self.update_team_status(status)
            elif "update_current_op_status" in message:
                self.update_status(status)
            elif "add_team_member" in message:
                self.add_team_member(member)

        except Exception as e:
            return {"error":str(e)}

    def clear_op(self):
        self.update_status("Off-Duty")
        self.update_team_status("Off-Duty")
        self.notify_team("Operation is cleared. You are officially Off-Duty.")
        self.team_members = []

    def new_op(self, team_members):
        self.clear_op()
        self.update_status("New Operation: Planning")
        self.update_status("Planning Operation")
        for member in team_members:
            self.add_team_member(member)
        self.notify_team("New Operation! Please stand by.")

    def update_status(self, status):
        """Update agent's mission status"""
        self.mission_status = status
        return {"status": "updated", "new_status": status}

    def get_status(self):
        """Return current status"""
        return getattr(self, "status", "Unknown")

    def update_team_status(self, status):
        self.team_status = status
        self.notify_team("Team status updated: " + status)

    def add_team_member(self, rescuer):
        self.team_members.append(rescuer)
        self.notify_team("New Team Member added: " + rescuer)

    def get_team_members(self):
        return getattr(self, "team_members", "Unknown")

    def get_team_status(self):
        return getattr(self, "team_status", "Unknown")

    def notify_team(self, message):
        return "Team Notified of message: " + message
