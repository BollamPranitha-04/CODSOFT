import os

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Mark Item as Completed")
    print("5. Exit")

def view_list(to_do_list):
    if not to_do_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, item in enumerate(to_do_list, start=1):
            status = "✓" if item['completed'] else "✗"
            print(f"{i}. [{status}] {item['task']}")

def add_item(to_do_list):
    task = input("\nEnter the task you want to add: ")
    to_do_list.append({"task": task, "completed": False})
    print(f'"{task}" has been added to your to-do list.')

def remove_item(to_do_list):
    view_list(to_do_list)
    if to_do_list:
        try:
            index = int(input("\nEnter the number of the task you want to remove: "))
            if 1 <= index <= len(to_do_list):
                removed = to_do_list.pop(index - 1)
                print(f'"{removed["task"]}" has been removed from your to-do list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def mark_as_completed(to_do_list):
    view_list(to_do_list)
    if to_do_list:
        try:
            index = int(input("\nEnter the number of the task you want to mark as completed: "))
            if 1 <= index <= len(to_do_list):
                to_do_list[index - 1]['completed'] = True
                print(f'"{to_do_list[index - 1]["task"]}" has been marked as completed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    to_do_list = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_list(to_do_list)
            elif choice == 2:
                add_item(to_do_list)
            elif choice == 3:
                remove_item(to_do_list)
            elif choice == 4:
                mark_as_completed(to_do_list)
            elif choice == 5:
                print("Exiting the to-do list application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
