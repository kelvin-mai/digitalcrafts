class Restaurant:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.itemsOrdered = 0

    def print_description(self):
        print(self.title)
        print(self.description)

    def order(self):
        self.itemsOrdered += 1

    def displayOrderStatus(self):
        print('We ordered ' + str(self.itemsOrdered) + 'And item was ' + str(self.title))

hala = Restaurant('Hala hala', 'This is a grand restaurant on a private island.')
hala.print_description()

bob = Restaurant("Bob's Burger", 'The best burger joint in town')
bob.print_description()
bob.order()
bob.displayOrderStatus()
