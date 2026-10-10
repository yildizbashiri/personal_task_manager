name = input("Enter your name: ")

print("Welcome", name)
tasks = []
while True:
    task = input("Enter a task(or exit): ")
    if task == "exit":
        break
    tasks.append(task)

print("your tasks")

for task in tasks:
    print(task) 