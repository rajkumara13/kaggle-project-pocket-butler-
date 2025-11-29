from fastapi import APIRouter
from backend.models.schemas import MealRequest
from utils.gemini_client import ask_gemini

router = APIRouter(prefix="/full-bundle", tags=["Pocket Butler Full Pipeline"])

@router.post("/")
def full(req: MealRequest):

    # Step 1 – Meal Plan
    meal_prompt = f"""
    Create a {req.days}-day meal plan.
    Preferences: {req.preferences}
    Return JSON structure.
    """
    meal_plan = ask_gemini(meal_prompt)

    # Step 2 – Grocery List
    grocery_prompt = f"""
    Generate grocery list for:
    {meal_plan}
    Return JSON.
    """
    grocery_list = ask_gemini(grocery_prompt)

    # Step 3 – Schedule
    schedule_prompt = f"""
    Create timeline for:
    {meal_plan}
    Return JSON.
    """
    schedule = ask_gemini(schedule_prompt)

    return {
        "meal_plan": meal_plan,
        "grocery_list": grocery_list,
        "schedule": schedule
    }
