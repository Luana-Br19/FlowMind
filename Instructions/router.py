from agents.finance_agent import FinanceAgent
from agents.general_agent import GeneralAgent
from agents.workshop_agent import WorkshopAgent
from agents.meeting_agent import MeetingAgent
from agents.idea_agent import IdeaAgent
from agents.geschaeftsreise_agent import GeschaeftsreiseAgent

# Router-Klasse, die den Plan ausführt und den entsprechenden Agenten auswählt
class Router:

    def execute(self, plan, intake):
        
        self.agents = {
            "finance": FinanceAgent(plan.category),
            "workshop": WorkshopAgent(plan.category),
            "meeting": MeetingAgent(plan.category),
            "ideas": IdeaAgent(plan.category),
            "geschaeftsreise": GeschaeftsreiseAgent(plan.category),
            "general": GeneralAgent(plan.category)
}

        agent = self.agents.get(plan.category)
        if not agent:
            raise ValueError(f"Unbekannte Kategorie: {plan.category}")

        return agent.execute(intake)