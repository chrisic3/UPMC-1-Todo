user_action_prompt = "Type add, show, edit, complete or exit: "
enter_todo_prompt = "Enter a new todo: "
edit_todo_prompt = "Enter the number of the todo you would like to edit: "
complete_todo_prompt = "Enter the number of the todo you would like to complete: "

while True:
    user_action = input(user_action_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo_item = input(enter_todo_prompt) + '\n'

            # file = open("todos.txt", 'r')
            # todo_list = file.readlines()
            # file.close()

            # Changed to with context manager
            with open("todos.txt", 'r') as file:
                todo_list = file.readlines()
            
            todo_list.append(todo_item)

            with open("todos.txt", 'w') as file:
                file.writelines(todo_list)
        case "show":
            with open("todos.txt", 'r') as file:
                todo_list = file.readlines()
            
            # List comprehension
            # todo_list = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            # Cast str input to int
            edit_todo_number = int(input(edit_todo_prompt))

            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that
            edit_todo_number = edit_todo_number - 1

            with open("todos.txt", 'r') as file:
                todo_list = file.readlines()
            
            new_todo_item = input(enter_todo_prompt)
            todo_list[edit_todo_number] = new_todo_item + '\n'

            with open("todos.txt", 'w') as file:
                file.writelines(todo_list)
        case "complete":
            # Cast str input to int
            complete_todo_number = int(input(complete_todo_prompt))

            with open("todos.txt", 'r') as file:
                todo_list = file.readlines()

            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that. Also store the item to print out later.
            #   Also remove the new line character.
            removed_todo = todo_list.pop(complete_todo_number - 1).strip('\n')
            print(f'The item "{removed_todo}" was removed from the list.')

            with open("todos.txt", 'w') as file:
                file.writelines(todo_list)
        case "exit":
            break

print("Bye")