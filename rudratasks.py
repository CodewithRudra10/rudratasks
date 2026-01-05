# RudraTasks🎯
# A simple To-Do-List app by Rudra
# Version 1.0- January 2026

tasks=["learn enumerate","solve maths","do homework","call a friend"]
print("=== Welcome to Rudra Tasks 🚀 ===")
print("To-Do-List:")
while True:
    user_input=input("enter the tasks :") .strip()
    if user_input.lower()=="done":
        print("quit")
        break
    if user_input:
     tasks.append(user_input)
     print(f"Added ✅  :  {user_input}")
    else:
        print("   ⚠️ Empty Task Skipped!")
    
    
for index,task in enumerate(tasks, start=1):
     print(f"{index}.[ ] {task}")

print("Keep grinding💪")
print("Built by Rudra in 2026🎯")

