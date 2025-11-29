import os
import json

MEMORY_FILE = "memory.json"

class MemoryStore:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            self.save({"preferences": {}, "history": []})

    def load(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_preference(self, key, value):
        data = self.load()
        data["preferences"][key] = value
        self.save(data)

    def add_history(self, record):
        data = self.load()
        data["history"].append(record)
        self.save(data)
