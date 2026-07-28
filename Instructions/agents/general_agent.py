from agents.base_agent import BaseAgent
from models.result import AgentResult

# Agent, der allgemeine Dokumente verarbeitet
class GeneralAgent(BaseAgent):

    def execute(self, intake):

        print("General Agent arbeitet...")

        document_text = ""

        if intake.attachments:
            document_text = self.pdf_service.attachment_reader(intake)

        response = self.llm.ask(

            system_prompt=open(
                "prompts/00-Router-Agent.md",
                encoding="utf-8"
            ).read(),

            user_prompt=f"""
                Slack Nachricht:
                {intake.text}
                Dokument Inhalt:
                {document_text}
                """
        )

        intake.tag = response.strip('{""}')
        print(intake.tag)

        return AgentResult(
            success=True,
            category=intake.tag,
            folder="none",
            filename="none",
            title="none",
            tags="none",
        )