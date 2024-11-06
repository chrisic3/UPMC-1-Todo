# Function to open a file and read the lines to a list
def get_todos(filepath="todos.txt"):
    """ Read a list of items from a text file. """
    # file = open("todos.txt", 'r')
    # todo_list = file.readlines()
    # file.close()

    # Changed to with context manager
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()

    return todo_list_local


# Function to open a file and read the lines to a list
def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a list of items to a text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)