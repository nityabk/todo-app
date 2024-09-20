#from modules import get_todos, write_todos
from pprint import pprint

import modules
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    # Get user input and strip space chars from it.
    user = input("to add,show,edit,complete or exit:")
    user = user.strip()

    if user.startswith("add"):
        todo = user[4:]

        todos = modules.get_todos()

        todos.append(todo + '\n')

        modules.write_todos(todos, 'todos.txt')

    elif user.startswith("show"):
        todos = modules.get_todos()
        # new_todos=[item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user.startswith("edit"):
        try:
            number = int(user[5:])
            print(number)

            number = number - 1
            todos = modules.get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'
            modules.write_todos(todos, 'todos.txt')
        except ValueError:
            print("Your command is not valid")
            continue

    elif user.startswith("complete"):
        try:
            number = int(user[9:])

            todos = modules.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            modules.write_todos(todos, 'todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list"
            print("message")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user.startswith("exit"):
        break
    else:
        print("not valid")
print('bye')
