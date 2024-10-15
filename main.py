user_action_prompt = "Type add, view, or exit:"
enter_todo_prompt = "Enter a todo:"

todos = []

while True:
    user_action = input(user_action_prompt).strip()

    match user_action:
        case "add":
            todo = input(enter_todo_prompt)
            todos.append(todo)
        case "view":
            for item in todos:
                print(item)
        case "exit":
            break

print("Bye")