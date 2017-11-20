class ShoppingList(object):
    def __init__(self, store = ''):
        self.store = store
        self.items = []
    def add_item(self, items):
        for item in items:
            self.items.append(item)
    def print_items(self):
        print(self.store)
        for item in self.items:
            print(item)

class Groceries(object):
    def __init__(self, lists = []):
        self.lists = lists

groceries = Groceries([
    ShoppingList('Fiesta'),
    ShoppingList('Walmart'),
    ShoppingList('Sams Club')
])

groceries.lists[0].items.append(['Milk', 'Soda', 'Fish'])
groceries.lists[1].items.append(['Paper', 'Napkins', 'Plate', 'Chips'])
groceries.lists[2].items.append(['Chicken','Beef','Eggs','Sugar','Salt','Pepper','Honey'])

for lists in groceries.lists:
    lists.print_items()
