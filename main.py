from dotenv import load_dotenv
import os
from tasks import show_tasks
name = input("Enter your name: ")

print("Welcome", name)
admin = input("Enter Admin Mode? (yes/no): ")

if admin == "yes":
    password = input("Enter password: ")

    if password == os.getenv("TASK_MANAGER_ADMIN_PASSWORD"):
        print("Admin login successful")
    else:
        print("Wrong password")
tasks = []
while True:
    task = input("Enter a task(or exit): ")
    if task == "exit":
        break
    priority = input("Enter priority (low/medium/high): ")
    while priority != "low" and priority != "medium" and priority != "high":
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ")
    tasks.append(task)
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()

print("your tasks")

for task in tasks:
    print(task) 

show_tasks(tasks)
load_dotenv()