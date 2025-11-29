from meal_planner import MealPlannerAgent

def test_meal_plan():
    agent = MealPlannerAgent()
    result = agent.generate_meal_plan(1)
    assert len(result) > 5
