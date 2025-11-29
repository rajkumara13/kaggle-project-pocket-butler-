from api_config import genai, MODEL


class SchedulerAgent:

    def schedule_meals(self, meal_plan_json):
        prompt = f"""
Create a daily meal schedule (timeline) for this meal plan:
Include: date, breakfast_time, lunch_time, dinner_time.
Return JSON only.

Meal Plan:
{meal_plan_json}
"""

        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)

        return response.text
