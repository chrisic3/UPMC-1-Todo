user_action_prompt = "Type add, view, or exit:"
enter_todo_prompt = "Enter a to-do:"

todos = []

while True:
    user_action = input(user_action_prompt)
    match user_action:
        case "add":
            todo = input(enter_todo_prompt)
            todos.append(todo)
        case "view":
            print(todos)
        case "exit":
            break

print("Bye")