from grocery_agent import GroceryAgent

def test_grocery():
    agent = GroceryAgent()
    plan = '{"breakfast": "idli"}'
    result = agent.generate_grocery_list(plan)
    assert "idli" in result
