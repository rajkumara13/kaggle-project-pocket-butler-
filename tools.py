import json

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def pretty(text):
    print("\n" + "="*50)
    print(text)
    print("="*50 + "\n")
