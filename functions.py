FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ READ A TEXT FILE AND RETURN THE LIST OF
        TO-DO ITEMS

    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in the next file."""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
