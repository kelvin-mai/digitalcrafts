class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start(self):
        print('Starting the gas car')

class ElectricCar(Car):
    def __init__(self):
        super(ElectricCar, self).__init__('Tesla','X')
    def start(self):
        print('Starting the electric car')

ec = ElectricCar()
print(ec.make)
print(ec.model)
ec.start()
