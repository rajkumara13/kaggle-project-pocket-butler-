from api_config import genai, MODEL


class GroceryAgent:

    def generate_grocery_list(self, meal_plan_json):
        prompt = f"""
Generate a grocery shopping list based on this meal plan.
Group into: vegetables, fruits, grains, protein, spices, dairy.
Return structured JSON only.

Meal Plan:
{meal_plan_json}
"""

        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)

        return response.text
