# inheritence lecture

class Animal(object):
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def run(self):
        print('running like a normal animal')
    def walk(self):
        print(self.name + " is walking")
    def eat(self):
        print(self.name + " is eating")

class Cheetah(Animal):
    def __init__(self):
        super(Cheetah,self).__init__('Cheetah', 'Cats')
        # Animal.__init__(self,'Cheetah', 'Cats')
    def run(self):
        print("Cheetah is running super fast")

cat = Animal('Lync', 'Cat Species')
cat.walk()
cat.eat()

ch = Cheetah()
ch.run()
