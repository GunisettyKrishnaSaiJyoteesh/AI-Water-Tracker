from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history
from src.logger import log_message

app = FastAPI()
agent = WaterIntakeAgent()

class waterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

@app.post("/logIntake")
async def logWaterIntake(request: waterIntakeRequest):
    log_intake(request.user_id, request.intake_ml)
    analysis = agent.analyze_intake(request.intake_ml)
    log_message(request.user_id, request.intake_ml)
    return {"message": "Water intake logged successfully.","analysis" : analysis}

@app.get("/history/{user_id}")
async def getWaterIntakeHistory(user_id: str):
    history = get_intake_history(user_id)
    return {"user_id": user_id, "history": history}