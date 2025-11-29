from meal_planner import MealPlannerAgent
from grocery_agent import GroceryAgent
from scheduler_agent import SchedulerAgent
from memory import MemoryStore
from tools import pretty

def run_pocket_butler():

    pretty("POCKET BUTLER — GEMINI AI VERSION")

    memory = MemoryStore()

    meal_agent = MealPlannerAgent()
    grocery_agent = GroceryAgent()
    scheduler_agent = SchedulerAgent()

    # Step 1: Generate meal plan
    meal_plan = meal_agent.generate_meal_plan(
        days=3,
        preferences="high protein, low sugar"
    )
    pretty("MEAL PLAN")
    pretty(meal_plan)

    memory.add_history({"meal_plan": meal_plan})

    # Step 2: Generate grocery list
    grocery_list = grocery_agent.generate_grocery_list(meal_plan)
    pretty("GROCERY LIST")
    pretty(grocery_list)

    # Step 3: Generate schedule
    schedule = scheduler_agent.schedule_meals(meal_plan)
    pretty("MEAL SCHEDULE")
    pretty(schedule)


if __name__ == "__main__":
    run_pocket_butler()
