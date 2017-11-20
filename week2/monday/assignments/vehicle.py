class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print(str(self.year) + ' ' + self.make + ' ' + self.model)

car = Vehicle('Nissan','Leaf',2015)
car.print_info()
