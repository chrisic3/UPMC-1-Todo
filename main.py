user_action_prompt = "Type add, show, edit, complete or exit:"
enter_todo_prompt = "Enter a new todo:"
edit_todo_prompt = "Enter the number of the todo you would like to edit:"
complete_todo_prompt = "Enter the number of the todo you would like to complete:"

while True:
    user_action = input(user_action_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo_item = input(enter_todo_prompt) + '\n'
            
            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()
            
            todo_list.append(todo_item)
            
            file = open("todos.txt", 'w')
            file.writelines(todo_list)
            file.close()
        case "show":
            for index, item in enumerate(todo_list):
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