FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of
    to-do- item.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(__name__)  note it equals __main__


# to test the script and will not appear in the main program
if __name__ == '__main__':
    print(get_todos())