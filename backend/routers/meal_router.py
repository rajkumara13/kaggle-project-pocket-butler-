from fastapi import APIRouter
from backend.models.schemas import MealRequest
from utils.gemini_client import ask_gemini

router = APIRouter(prefix="/meal-plan", tags=["Meal Planner"])

@router.post("/")
def generate_meal_plan(req: MealRequest):
    
    prompt = f"""
    Create a healthy meal plan for {req.days} days.
    Preferences: {req.preferences}
    Return JSON with breakfast, lunch, dinner.
    """
    output = ask_gemini(prompt)
    return {"meal_plan": output}
