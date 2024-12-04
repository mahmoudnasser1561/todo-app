import functions
import  FreeSimpleGUI as Sg
import  time

clock = Sg.Text('', key='clock')

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
exit_button = Sg.Button("Exit")

complete_button = Sg.Button("Complete")

window = Sg.Window("My To-Do App",
                   layout=[
                            [clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window['clock'].update(value=now)

    print(event)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit  = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                # print("please select an Item")
                Sg.popup("Please Select an Item First.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todo"].update(value='')
                window["todos"].update(values=todos)
            except IndexError:
                Sg.popup("Please select an Item First", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WIN_CLOSED:
            break

window.close()