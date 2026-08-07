from agents.base_agent import BaseAgent
from models.result import AgentResult
import json
from pathlib import Path
from services.travel_excel_service3 import TravelExcelService

class GeschaeftsreiseAgent(BaseAgent):

    def execute(self, intake):

        print("Geschäftsreise Agent arbeitet...")

        document_text = ""

        if intake.attachments:

            document_text = self.pdf_service.attachment_reader(intake)

        tree = self.folder_service.get_tree()

        path = "prompts/04-Geschaeftsreise-Agent03.md"
        response = self.execute_llm(path, intake, document_text, tree)

        data = self.load_json(response, intake)
        excel_path = Path(
        "../Inbox",
        data["folder"],
        "Reiseübersicht.xlsx"
        )

        excel = TravelExcelService(excel_path)
#        print("Hello")
        #excel = TravelExcelService()
#        excel.update(data)

		# excel = TravelExcelService()
        # excel.update(data)

        return self.agent_result(data, intake)
