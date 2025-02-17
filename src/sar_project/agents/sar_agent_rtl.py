from sar_project.agents.base_agent import SARBaseAgent
from sar_project.agents.rescuer_agent import RescuerAgent
from google import genai
import os
from dotenv import load_dotenv, dotenv_values


class RTLAgent(SARBaseAgent):

    def __init__(self, name="rtl_agent"):
        load_dotenv()
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
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    def process_request(self, message, status=None, member=None, members=[]):
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
                self.new_op(members)
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
        return {"op_cleared": True}

    def new_op(self, team_members):
        self.clear_op()
        self.update_team_status("New Operation: Planning")
        self.update_status("Planning Operation")
        for member in team_members:
            self.add_team_member(member)
        self.notify_team("New Operation! Please stand by.")
        return {"new_op_created": True}

    def update_status(self, status):
        """Update agent's mission status"""
        self.mission_status = status
        message = self.generate_message("Mission status updated: " + status)
        self.notify_team(message)
        return {"status": "updated", "new_status": status}

    def get_status(self):
        """Return current status"""
        return getattr(self, "status", "Unknown")

    def update_team_status(self, status):
        self.team_status = status
        self.notify_team("Team status updated: " + status)
        return {"team_status": "updated", "new_team_status": status}

    def add_team_member(self, rescuer_name):
        self.team_members.append(RescuerAgent(name=rescuer_name))
        self.notify_team("New Team Member added: " + rescuer_name)
        return {"team_member_added": True}

    def get_team_members(self):
        return getattr(self, "team_members", "Unknown")

    def get_team_status(self):
        return getattr(self, "team_status", "Unknown")

    def notify_team(self, message):
        """Not yet implemented; Will create a dummy Rescuer agent that can receive messages"""
        for member in self.team_members:
            member.message(message)
        return "Message sent"


    def generate_message(self, message):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Notify a team of rescuers of the message: \"" + message +
                     "\", and provide recommendations for safety and efficiency."
        )
        return response.text