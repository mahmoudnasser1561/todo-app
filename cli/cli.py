from src.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)

while True:
    user_action = input("Tye add, show, edit, complete: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for idx, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{idx + 1} {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")