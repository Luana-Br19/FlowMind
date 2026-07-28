from agents.base_agent import BaseAgent
from models.result import AgentResult
from services.llm_service import LLMService
from services.pdf_service import PDFService

# Agent, der Finanzdokumente verarbeitet
class FinanceAgent(BaseAgent):

    def execute(self, intake):

        print("Finanz Agent arbeitet...")

        document_text = ""

        if intake.attachments:

            document_text = self.pdf_service.attachment_reader(intake)

        tree = self.folder_service.get_tree()

        path = "prompts/05-Finance-Agent02.md"
        response = self.execute_llm(path, intake, document_text, tree)

        data = self.load_json(response)

        return self.agent_result(data, intake)