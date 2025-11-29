class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            return "No tasks added."
        return "\n".join([f"{i+1}. {t}" for i, t in enumerate(self.tasks)])

task_manager = TaskManager()
