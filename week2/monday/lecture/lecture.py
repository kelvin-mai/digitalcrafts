class Person:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = ''

    def printAttributes(self):
        print(self.firstName)
        print(self.lastName)
        print(self.middleName)

    def walk(self):
        print("person is walking")

    def sing(self,songName):
        print("Person is singing " + songName)

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.noOfCylinders = 4
    def start(self): #always include 'self' in python class functions
        print('Starting Car')

bmw = Car('BMW', 'Series 3')
# print(bmw.make)
# print(bmw.model)
# print(bmw.noOfCylinders)
# bmw.start()
#
# toyota = Car('Toyota', 'Camry')
# print(toyota.make)
# print(toyota.model)

john = Person('John', 'Doe')
john.printAttributes()
# if you have skipped arguments, use named arguments
# eg. person(firstname = 'john', lastname = 'doe')
john.middleName = 'Danger'
john.printAttributes()
john.walk()
john.sing('Happy Birthday')
