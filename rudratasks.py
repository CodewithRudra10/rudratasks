# Rudra's Simple To-Do List App 🎯
# Built by Rudra  - January 2026

tasks = []  # Global list to store all tasks

def add_task():
    global tasks
    task = input("➕ Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"   ✅ Added: {task}")
    else:
        print("   ⚠️ Empty task skipped!")

def view_tasks():
    if not tasks:
        print("   📭 No tasks yet! Add one first.")
        return
    
    print("\n   🎯 Your To-Do List:")
    print("   " + "-" * 30)
    for index, item in enumerate(tasks, start=1):
        status = "[✓]" if item["done"] else "[ ]"
        print(f"   {index}. {status} {item['task']}")
    print()

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("   Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"   🎉 Task {num} marked as done!")
        else:
            print("   ❌ Invalid number!")
    except ValueError:
        print("   ❌ Please enter a number!")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("   Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"   🗑️ Deleted: {removed['task']}")
        else:
            print("   ❌ Invalid number!")
    except ValueError:
        print("   ❌ Please enter a number!")

# === Main App Loop ===
print("=== Welcome to Rudra's Simple To-Do List 🎯 ===\n")

while True:
    print("What do you want to do?")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Quit")
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("\nKeep grinding, Founder! See you next time 💪")
        break
    else:
        print("❌ Invalid choice — try again!")

print("App closed. All tasks saved in memory.")
