class MemoryStore:
    def __init__(self):
        self.memory = []

    def remember(self, info):
        self.memory.append(info)

    def recall(self):
        if not self.memory:
            return "Memory is empty."
        return "\n".join(self.memory)

user_memory = MemoryStore()
