# Function to open a file and read the lines to a list
def get_todos(filepath):
    # file = open("todos.txt", 'r')
    # todo_list = file.readlines()
    # file.close()

    # Changed to with context manager
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()

    return todo_list_local


user_action_prompt = "Type add, show, edit, complete, or exit: "
enter_todo_prompt = "Enter a new todo: "
edit_todo_prompt = "Enter the number of the todo you would like to edit: "
complete_todo_prompt = "Enter the number of the todo you would like to complete: "

while True:
    user_action = input(user_action_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # Since the input should be "add {todo item}", 
        #   split the string to get everything after 
        #   "add "
        todo_item = user_action[4:]

        todo_list = get_todos("todos.txt")
        
        todo_list.append(todo_item + '\n')

        with open("todos.txt", 'w') as file:
            file.writelines(todo_list)
    elif user_action.startswith("show"):
        todo_list = get_todos("todos.txt")
        
        # List comprehension
        # todo_list = [item.strip('\n') for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            # Same reason for string split as in the "add" feature
            # Cast str input to int
            edit_todo_number = int(user_action[5:])

            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that
            edit_todo_number = edit_todo_number - 1

            todo_list = get_todos("todos.txt")
            
            new_todo_item = input(enter_todo_prompt)
            todo_list[edit_todo_number] = new_todo_item + '\n'

            with open("todos.txt", 'w') as file:
                file.writelines(todo_list)
        except ValueError:
            print("Invalid command")
            continue
    elif user_action.startswith("complete"):
        try:
            # Same reason for the string split as in the "add" feature
            # Cast str input to int
            complete_todo_number = int(user_action[9:])

            todo_list = get_todos("todos.txt")

            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that. Also store the item to print out later.
            #   Also remove the new line character.
            removed_todo = todo_list.pop(complete_todo_number - 1).strip('\n')
            print(f'The item "{removed_todo}" was removed from the list.')

            with open("todos.txt", 'w') as file:
                file.writelines(todo_list)
        except IndexError:
            print("There is not item at that number.")
    elif user_action.startswith("exit"):
        break
    else:
        print("Illegal input")

print("Bye")