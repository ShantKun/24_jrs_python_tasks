Tasks = [] 

def create_task():
    Title = input("Enter the title of the task: ")
    Description = input("Enter the description of the task: ")
    task = {"Title": Title, "Description": Description}
    Tasks.append(task) 
    print("Task created successfully!")

def view_task():
    if Tasks:
        print("Tasks:")
        for idx, task in enumerate(Tasks, start=1):
            print(f"{idx}. Title: {task['Title']}, Description: {task['Description']}")
    else:
        print("No tasks available")

def update_task():
    view_task()
    if Tasks:
        task_index = int(input("Enter the index of the task you want to update: "))
        if 0 <= task_index < len(Tasks):
            new_title = input("Enter new Title: ")
            new_description = input("Enter new Description: ")
            if new_title:
                Tasks[task_index]['Title'] = new_title
            if new_description:
                Tasks[task_index]['Description'] = new_description
            print("Task Updated successfully")
        else:
            print("Invalid Task Index.")
    else:
        print("No tasks available to update.")

def delete_task():
    view_task()
    if Tasks:
        task_index = int(input("Enter the number of the task that you want to delete: "))
        if 0 <= task_index < len(Tasks):
            deleted_task = Tasks.pop(task_index)
            print(f"Task '{deleted_task['Title']}' deleted successfully!")
        else:
            print("Invalid Task Index.")
    else:
        print("No tasks available to delete.")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    opt = input("Enter input (1-5): ")  

    if opt == '1':
        create_task()
    elif opt == '2':
        view_task()
    elif opt == '3':
        update_task()
    elif opt == '4':
        delete_task()
    elif opt == '5':
        print("Exit from Task Manager :)")
        break
    else:
        print("Invalid Input! Enter valid input (1-5)")
