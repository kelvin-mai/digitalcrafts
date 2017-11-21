import json

class Task(object):
    def __init__(self,title):
        self.title = title
    def toDictionary(self):
        return { "title":self.title }

newTask = Task('Mail the stuff')

filename = 'tasks.json'

task1 = {"title" : "wash the car", "priority": "high"}
task2 = {"title" : "feed cat", "priority": "low"}

tasks = [task1, task2]

with open(filename, 'w') as file_object:
    json.dump(newTask.toDictionary(), file_object, sort_keys=True, indent=4)

with open(filename) as file_object:
    contents = json.load(file_object)
    # print(contents[0])
    # print(contents)
