from agents.base_agent import BaseAgent
from models.result import AgentResult

# Agent, der allgemeine Dokumente verarbeitet
class GeneralAgent(BaseAgent):

    def execute(self, intake):

        print("General Agent arbeitet...")

        return AgentResult(
            success=True,
            category="general",
            message="Allgemeines Dokument verarbeitet."
        )