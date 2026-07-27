from agents.finance_agent import FinanceAgent
from agents.general_agent import GeneralAgent
from agents.workshop_agent import WorkshopAgent

# Router-Klasse, die den Plan ausführt und den entsprechenden Agenten auswählt
class Router:

    def execute(self, plan, intake):
        
        self.agents = {
            "finance": FinanceAgent(),
            "workshop": WorkshopAgent(),
            #"health": HealthAgent(),
            "general": GeneralAgent()
}

        agent = self.agents.get(plan.category)
        if not agent:
            raise ValueError(f"Unbekannte Kategorie: {plan.category}")

        return agent.execute(intake)