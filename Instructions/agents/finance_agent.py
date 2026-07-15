from agents.base_agent import BaseAgent
from models.result import AgentResult

# Agent, der Finanzdokumente verarbeitet
class FinanceAgent(BaseAgent):

    def execute(self, intake):

        print("Finance Agent arbeitet...")

        return AgentResult(
            success=True,
            category="finance",
            message="Finanzdokument verarbeitet."
        )