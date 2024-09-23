import cli
import FreeSimpleGUI as sg

add_button = sg.Button("Add")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = cli.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            cli.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
