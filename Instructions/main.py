import json
import sys

from models.intake_item import IntakeItem
from planner import Planner
from router import Router
from services.git_service import GitService

import os


def check_files(intake):

    for file in intake.attachments:

        if os.path.exists(file):

            print(
              f"[OK] Datei gefunden: {file}"
            )
        else:
            print(
              f"[ERROR] Datei fehlt: {file}"
            )

def process_intake(intake: IntakeItem):

    print("[INFO] Planner wird gestartet...")

    planner = Planner()
    plan = planner.create_plan(intake)

    print(f"[INFO] Kategorie erkannt: {plan.category}")
    cat = plan.category

    print("[INFO] Router wird gestartet...")

    router = Router()
    result = router.execute(plan, intake)

    if cat == "general":
        plan.category = result.category
        print(f"[INFO] NEUE Kategorie erkannt: {plan.category}")
        result = router.execute(plan, intake)

    return result

def git_push(result):
    git = GitService()

    git.push(
        category=result.category,
        title=result.title
    )

def main():

    if len(sys.argv) < 2:
        print("Verwendung: python3 main.py input.json")
        return

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    intake = IntakeItem(
        text=data.get("text", ""),
        tags=data.get("tags", []),
        attachments=data.get("attachments", ""),
        input_type=data.get("type", ""),
        id=data.get("id", ""),
        user=data.get("user", ""),
        source=data.get("source", "Slack"),
        channel=data.get("channel", ""),
        
    )

    check_files(intake)
    print("[INFO] Neue Anfrage erhalten")
    print(f"Text: {intake.text}")
    print(f"Tags: {intake.tags}")
    print()

    result = process_intake(intake)
    git_push(result)

    print()
    print("========== ERGEBNIS ==========")
    print(result)
    print("PROCESS BEENDET")

    #return


if __name__ == "__main__":
    main()
