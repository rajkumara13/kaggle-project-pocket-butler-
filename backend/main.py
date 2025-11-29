from backend.utils.chat import ai_chat
from backend.utils.tasks import task_manager
from backend.utils.memory import user_memory
from backend.utils.voice import speak
from backend.utils.web_search import smart_search

# Command handlers
def handle_add_task(args):
    task_manager.add_task(args)
    print("Task added!")

def handle_show_tasks(args):
    print(task_manager.show_tasks())

def handle_search(args):
    try:
        result = smart_search(args)
        print(result)
    except Exception as e:
        print("Search failed:", e)

def handle_remember(args):
    user_memory.remember(args)
    print("Saved to memory.")

def handle_recall(args):
    print(user_memory.recall())

# Command mapping
COMMANDS = {
    "add task": handle_add_task,
    "show tasks": handle_show_tasks,
    "search": handle_search,
    "remember": handle_remember,
    "recall": handle_recall,
}

def main():
    print("=== Pocket Butler AI ===")

    while True:
        command = input("\nYou: ").strip()

        if command.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! 🧤")
            break

        # Match against known commands
        matched = False
        for key, func in COMMANDS.items():
            if command.lower().startswith(key):
                args = command[len(key):].strip()
                func(args)
                matched = True
                break

        # Default AI chat if no command matched
        if not matched:
            try:
                response = ai_chat(command)
                print("AI:", response)
                speak(response)
            except Exception as e:
                print("AI chat failed:", e)

if __name__ == "__main__":
    main()