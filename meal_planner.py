from api_config import genai, MODEL


class MealPlannerAgent:

    def generate_meal_plan(self, days, preferences=""):
        prompt = f"""
Create a healthy meal plan for {days} days.
User preferences: {preferences}.
Return as JSON with fields: breakfast, lunch, dinner.
"""

        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)

        return response.text
