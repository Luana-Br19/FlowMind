from models.plan import Plan

# Klasse, die den Planungsprozess für die Verarbeitung von Dokumenten übernimmt 
class Planner:

    def create_plan(self, intake):

        if "finance" in intake.tags:

            return Plan(
                category="finance",
                # tasks=[
                #     "extract",
                #     "analyse",
                #     "write"
                # ]
            )
        elif "workshop" in intake.tags:
            
            return Plan(    
                category="workshop",
            )

        return Plan(
            category="general",
            # tasks=[
            #     "analyse",
            #     "write"
            # ]
        )