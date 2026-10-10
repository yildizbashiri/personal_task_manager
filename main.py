from tasks import show_tasks
name = input("Enter your name: ")

print("Welcome", name)
tasks = []
while True:
    task = input("Enter a task(or exit): ")
    if task == "exit":
        break
    tasks.append(task)
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()

print("your tasks")

for task in tasks:
    print(task) 

show_tasks(tasks)