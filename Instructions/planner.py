from models.plan import Plan

# Klasse, die den Planungsprozess für die Verarbeitung von Dokumenten übernimmt 
class Planner:

    def create_plan(self, intake):

        if "finance" in intake.tags:

            return Plan(
                category="finance",
                tasks=[
                    "extract",
                    "analyse",
                    "write"
                ]
            )

        return Plan(
            category="general",
            tasks=[
                "analyse",
                "write"
            ]
        )