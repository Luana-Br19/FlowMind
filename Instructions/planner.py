from models.plan import Plan

# Klasse, die den Planungsprozess für die Verarbeitung von Dokumenten übernimmt 
class Planner:

    def create_plan(self, intake):
        category = intake.tags
        cat = [wort.lower() for wort in category]

        if any(tag in cat for tag in ["finance", "finanzen"]):

            return Plan(
                category="finance",
            )

        if any(tag in cat for tag in ["workshop", "workshops"]):
            
            return Plan(    
                category="workshop",
            )
        
        if any(tag in cat for tag in ["idea", "ideas", "idee"]):
            
            return Plan(    
                category="ideas",
            )

        if any(tag in cat for tag in ["geschaeftsreise", "geschaeftsreisen"]):
            
            return Plan(    
                category="geschaeftsreise",
            )
        
        if any(tag in cat for tag in ["meeting", "meetings"]):
            
            return Plan(    
                category="meeting",
            )

        return Plan(
            category="general",
            # tasks=[
            #     "analyse",
            #     "write"
            # ]
        )