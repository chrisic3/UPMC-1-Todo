user_action_prompt = "Type add, show, edit, or exit:"
enter_todo_prompt = "Enter a new todo:"
todo_number_prompt = "Enter the number of the todo you would like to edit:"

todo_list = []

while True:
    user_action = input(user_action_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo_item = input(enter_todo_prompt)
            todo_list.append(todo_item)
        case "show":
            for item in todo_list:
                print(item)
        # TODO: Add case for "edit"
        #   Use numbers for indexing
        case "edit":
            # Cast str input to int
            todo_number = int(input(todo_number_prompt))
            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that
            todo_number = todo_number - 1
            new_todo_item = input(enter_todo_prompt)
            todo_list[todo_number] = new_todo_item
        case "exit":
            break

print("Bye")