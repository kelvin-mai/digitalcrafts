class TodoList(object):
    def __init__(self, todos = []):
        self.todos = todos
    def add_task(self, task):
        self.todos.append(task)
    def view_tasks(self):
        for task in self.todos:
            print(task)
    def remove_task(self, task):
        for i in range(0,len(self.todos)):
            if task == self.todos[i]:
                del self.todos[i]
                break

todos = TodoList()
def prompt():
    print("Select option")
    print("'add' to add task")
    print("'view' to view todo list")
    print("'remove' to remove task")
    print("'q' to quit")

print("Welcome to the todo list app")
prompt()
while True:
    choice = raw_input(">>")

    if choice == 'q':
        break
    elif choice == 'add':
        todos.add_task(raw_input('Input task to add: '))
    elif choice == 'view':
        todos.view_tasks()
    elif choice == 'remove':
        todos.remove_task(raw_input('Input task to remove: '))
    else:
        print("Invalid option")
        prompt()
