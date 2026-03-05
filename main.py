assignments = {}

while True:
    print("1.Assign 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == '1':
        engineer = input("Engineer: ")
        project = input("Project: ")
        assignments[engineer] = project
    elif ch == '2':
        print(assignments)
    elif ch == '3':
        break
