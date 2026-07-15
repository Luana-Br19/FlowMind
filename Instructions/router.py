from agents.finance_agent import FinanceAgent
from agents.general_agent import GeneralAgent

# Router-Klasse, die den Plan ausführt und den entsprechenden Agenten auswählt
class Router:

    def execute(self, plan, intake):

        # if plan.category == "finance":

        #     agent = FinanceAgent()

        # else:

        #     agent = GeneralAgent()
        
        self.agents = {
            "finance": FinanceAgent(),
            #"health": HealthAgent(),
            "general": GeneralAgent()
}

        agent = self.agents.get(plan.category)
        if not agent:
            raise ValueError(f"Unbekannte Kategorie: {plan.category}")

        return agent.execute(intake)