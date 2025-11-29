from fastapi import APIRouter
from backend.models.schemas import GroceryRequest
from utils.gemini_client import ask_gemini

router = APIRouter(prefix="/grocery-list", tags=["Grocery Agent"])

@router.post("/")
def generate_grocery(req: GroceryRequest):

    prompt = f"""
    Generate a grocery list based on this meal plan:
    {req.meal_plan}
    Return structured JSON only.
    """

    output = ask_gemini(prompt)
    return {"grocery_list": output}
