from fastapi import APIRouter
from backend.models.schemas import ScheduleRequest
from utils.gemini_client import ask_gemini

router = APIRouter(prefix="/schedule", tags=["Meal Scheduler"])

@router.post("/")
def meal_schedule(req: ScheduleRequest):

    prompt = f"""
    Create a daily meal timeline from the meal plan below.
    Include breakfast_time, lunch_time, dinner_time.
    Return JSON only.

    {req.meal_plan}
    """

    output = ask_gemini(prompt)
    return {"schedule": output}
