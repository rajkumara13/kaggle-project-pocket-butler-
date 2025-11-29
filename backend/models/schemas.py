from pydantic import BaseModel

class MealRequest(BaseModel):
    days: int
    preferences: str = ""

class GroceryRequest(BaseModel):
    meal_plan: str

class ScheduleRequest(BaseModel):
    meal_plan: str
