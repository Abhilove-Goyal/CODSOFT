to_do_list = []
def show_task():
    if len(to_do_list) == 0:
        print("No work to do, you can rest today!")
    else:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. Task: {list(task.keys())[0]}, Due: {list(task.values())[0]}")
    print("\n")

def remove_task():
    try:
        x = int(input("Enter the task number to remove: "))
        if 1 <= x <= len(to_do_list):
            removed_task = to_do_list.pop(x - 1)
            print(f"Removed task: {list(removed_task.keys())[0]}\n")

        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")

def add_task():
    key = input("Enter the task to do: ")
    due = input("Enter the due date for it: ")
    new_task = {key: due}
    to_do_list.append(new_task)
    print(f"Added task: {key}, Due: {due}\n")

def task_done():
    try:
        index = int(input("Enter the task number completed: "))
        if 1 <= index <= len(to_do_list):
            completed_task = list(to_do_list[index - 1].keys())[0]
            print(f"Task '{completed_task}' marked as completed.\n")
            to_do_list.pop(index - 1)
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")

def main():
    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print("\n")
        
        if choice == '1':
            show_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            task_done()
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
