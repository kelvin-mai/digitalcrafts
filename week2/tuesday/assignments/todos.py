import json
import os

def prompt():
    print("Select option")
    print("'1' to add new task")
    print("'2' to view remove task")
    print("'3' to quit")
def line():
    print('------------------------------')

class Task(object):
    def __init__(self, name):
        self.name = name
    def toDictionary(self):
        return {"name": self.name}

class TodoList(object):
    def __init__(self, todos = []):
        self.todos = todos
    def load(self, filename):
        with open(filename) as file_object:
            for item in json.load(file_object):
                self.todos.append(Task(item['name']))
    def add_task(self, task):
        print("Added '" + task + "' to todo list")
        self.todos.append(Task(task))
    def view_tasks(self):
        if len(self.todos) == 0:
            print("No items in todo list")
            return
        for task in self.todos:
            print(task.name)
    def remove_task(self, task):
        if task not in self.todos:
            print("Task not in todo list")
        for i in range(0,len(self.todos)):
            if task == self.todos[i]:
                print("Removed '" + task + "' from todo list")
                del self.todos[i]
                break
    def to_dictionary(self):
        arr = []
        for item in self.todos:
            arr.append(item.toDictionary())
        return arr

todolist = TodoList()
filename = 'todolist.json'

line()
print('Welcome to the to do list app')
line()

if not os.path.isfile(filename):
    with open(filename,'w') as file_object:
        file_object.write('')
if os.stat(filename).st_size != 0:
    todolist.load(filename)
todolist.view_tasks()

prompt()
while True:
    choice = raw_input(">> ")
    if choice == '1':
        todolist.add_task(raw_input('Input task to add: '))
    elif choice == '2':
        todolist.remove_task(raw_input('Input task to remove: '))
    elif choice == '3':
        break
    else:
        print('Invalid choice! Try again.')

line()
print('Current to do list')
todolist.view_tasks()
with open(filename,'w') as file_object:
    json.dump(todolist.to_dictionary(), file_object, sort_keys=True, indent=4)
