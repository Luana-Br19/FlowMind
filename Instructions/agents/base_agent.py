from abc import ABC, abstractmethod
import json
from services.llm_service import LLMService
from services.pdf_service import PDFService
from services.markdown_service import MarkdownService
from services.folder_service import FolderService
from models.result import AgentResult

class BaseAgent(ABC):

    def __init__(self, cat):
        self.llm = LLMService()
        self.pdf_service = PDFService()
        self.markdown_service = MarkdownService()
        self.folder_service = FolderService()
        self.agent_category = cat

    @abstractmethod
    def execute(self, intake):
        pass

    def execute_llm(self, path_prompt, intake, document_text, tree):
        response = self.llm.ask(
            system_prompt=open(
                path_prompt,
                encoding="utf-8"
            ).read(),

            user_prompt=f"""
                Slack Nachricht:
                {intake.text}
                Dokument Inhalt:
                {document_text}
                Aktuelle Ordnerstruktur:
                {tree}
                PDF-Path:
                {intake.attachments}
                """
        )
        response = self.alter_response(response)

        return response


    def alter_response(self, response):
        response = response.strip()
        
        if not response:
            raise ValueError("Claude hat eine leere Antwort geliefert.")
        
        if response.startswith("```json"):
            response = response.replace("```json", "", 1)
            response = response.replace("```", "", 1)
        
        return response

    def save_md(self, data, intake):

        markdown = self.markdown_service.create_markdown(data, intake) #result.content

        # self.markdown_service.save(
        #     data["folder"], #result.folder,
        #     data["filename"], #result.filename,
        #     markdown
        # )
        self.markdown_service.save(data, intake)

    def load_json(self, response, intake):
        #print(repr(response))
        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            raise ValueError("Claude hat kein gültiges JSON zurückgegeben.")

        self.save_md(data, intake)
        intake.category = self.agent_category

        return data

    def agent_result(self, data, intake):
        return AgentResult(
            success=True,
            category= self.agent_category, #intake.tags[0], #"workshop",
            folder=data["folder"],
            filename=data["filename"],
            title=data["title"],
            tags=data["tags"],
            #content=data
        )