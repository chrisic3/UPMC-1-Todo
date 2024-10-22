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
            new_todo_item = input(enter_todo_prompt)
            todo_list[edit_todo_number] = new_todo_item
        case "complete":
            # Cast str input to int
            complete_todo_number = int(input(complete_todo_prompt))
            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that
            todo_list.pop(complete_todo_number - 1)
        case "exit":
            break

print("Bye")