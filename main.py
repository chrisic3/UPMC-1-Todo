import functions
import time

user_action_prompt = "Type add, show, edit, complete, or exit: "
enter_todo_prompt = "Enter a new todo: "
edit_todo_prompt = "Enter the number of the todo you would like to edit: "
complete_todo_prompt = "Enter the number of the todo you would like to complete: "

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input(user_action_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # Since the input should be "add {todo item}", 
        #   split the string to get everything after 
        #   "add "
        todo_item = user_action[4:]

        todo_list = functions.get_todos()
        
        todo_list.append(todo_item + '\n')

        functions.write_todos(todo_list)
    elif user_action.startswith("show"):
        todo_list = functions.get_todos()
        
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

            todo_list = functions.get_todos()
            
            new_todo_item = input(enter_todo_prompt)
            todo_list[edit_todo_number] = new_todo_item + '\n'

            functions.write_todos(todo_list)
        except ValueError:
            print("Invalid command")
            continue
    elif user_action.startswith("complete"):
        try:
            # Same reason for the string split as in the "add" feature
            # Cast str input to int
            complete_todo_number = int(user_action[9:])

            todo_list = functions.get_todos()

            # Subtract 1 because the list starts at 0 and the user
            #   doesn't know that. Also store the item to print out later.
            #   Also remove the new line character.
            removed_todo = todo_list.pop(complete_todo_number - 1).strip('\n')

            functions.write_todos(todo_list)

            print(f'The item "{removed_todo}" was removed from the list.')
        except IndexError:
            print("There is not item at that number.")
    elif user_action.startswith("exit"):
        break
    else:
        print("Illegal input")

print("Bye")