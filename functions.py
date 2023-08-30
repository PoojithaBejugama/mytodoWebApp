def get_todos(filepath= "todos.txt"):
    """Read a text file and returna list of Todos"""
    # with conetxt manager - file closes automatically
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_in, filepath = "todos.txt"):
    """Write todo items to a text file"""
    with open('todos.txt', 'w') as file:
        file.writelines(todos_in)
