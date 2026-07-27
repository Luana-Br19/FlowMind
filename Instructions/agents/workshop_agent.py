from agents.base_agent import BaseAgent
from models.result import AgentResult
import json

class WorkshopAgent(BaseAgent):

    def execute(self, intake):

        print("Workshop Agent arbeitet...")

        document_text = ""

        if intake.attachments:

            document_text = self.pdf_service.attachment_reader(intake)

        tree = self.folder_service.get_tree()

        path = "prompts/01-Workshop-Agent02.md"
        response = self.execute_llm(path, intake, document_text, tree)

        data = self.load_json(response)

        return self.agent_result(data, intake)