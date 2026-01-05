
tasks=["learn enumerate","solve maths","do homework","call a friend"]
print("To-Do-List:")
while True:
    user_input=input("enter the tasks: (or type 'done' to quit):")
    if user_input.lower()=="done":
        print("quit")
        break
    tasks.append(user_input)
    
    
for index,task in enumerate(tasks, start=1):
     print(f"{index}.[ ] {task}")