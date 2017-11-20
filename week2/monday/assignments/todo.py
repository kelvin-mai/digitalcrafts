class TodoList(object):
    def __init__(self, todos = []):
        self.todos = todos
    def add_task(self, task):
        print("Added '" + task + "' to todo list")
        self.todos.append(task)
    def add_priority(self, task):
        print("Added '" + task + "' to todo list with priority")
        self.todos.insert(0,task)
    def view_tasks(self):
        if len(self.todos) == 0:
            print("No items in todo list")
            return
        for task in self.todos:
            print(task)
    def remove_task(self, task):
        if task not in self.todos:
            print("Task not in todo list")
        for i in range(0,len(self.todos)):
            if task == self.todos[i]:
                print("Removed '" + task + "' from todo list")
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
    elif choice.replace(' ','').lower() == 'add':
        priority = raw_input("Is it important? 'y' or 'n': ")
        if priority == 'y':
            todos.add_priority(raw_input('Input task to add: '))
        else:
            todos.add_task(raw_input('Input task to add: '))
    elif choice.replace(' ','').lower() == 'view':
        todos.view_tasks()
    elif choice.replace(' ','').lower() == 'remove':
        todos.remove_task(raw_input('Input task to remove: '))
    else:
        print("Invalid option"),
        prompt()
