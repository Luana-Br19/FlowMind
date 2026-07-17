from fastapi import FastAPI
from models.intake_item import IntakeItem
from main import process_intake

app = FastAPI()


@app.post("/process")
def process(item: IntakeItem):

    result = process_intake(item)

    return result