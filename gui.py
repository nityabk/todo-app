import functions
import FreeSimpleGUI as sg
add_button=sg.Button("Add")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
window = sg.Window('My To-Do App',layout=[[label],[input_box,add_button]])
window.read()
window.close()