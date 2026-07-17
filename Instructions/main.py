from models.intake_item import IntakeItem
from planner import Planner
from router import Router

# def main():

#     intake = IntakeItem(

#         text="Meine Steuerrechnung",

#         tags=["finance"],

#         attachments=["steuer.pdf"],

#         user="Philipp"

#     )

#     print("Neue Anfrage eingegangen")
#     print()

#     planner = Planner()

#     plan = planner.create_plan(intake)

#     print("Plan erstellt:")
#     print(plan)
#     print()

#     router = Router()

#     result = router.execute(plan, intake)

#     print("Ergebnis:")
#     print(result)


# if __name__ == "__main__":
#     main()

def process_intake(intake):

    planner = Planner()

    plan = planner.create_plan(intake)

    router = Router()

    result = router.execute(plan, intake)

    return result