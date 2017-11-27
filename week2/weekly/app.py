import datetime
import os
from pool_table import PoolTable
from pool_table import Tables

class App():
    def __init__(self):
        self.tables = Tables()
        self.filename  = datetime.date.today().strftime('%m-%d-%Y') + '.json'
        if os.path.isfile(self.filename):
            self.tables.load(self.filename)
        else:
            for i in range(12):
                self.tables.add_table(i)
        self.line = '--------------------------------------'
        self.prompt = """
        '1' to checkout table
        '2' to check in
        '3' to view tables
        '4' to quit
        """
        self.invalid = "Invalid choice, try again"
        self.run()

    def choice(self, choice):
        if choice == '1':
            self.checkout()
            return True
        elif choice == '2':
            self.checkin()
            return True
        elif choice == '3':
            self.tables.view_tables()
            return True
        elif choice == '4':
            return False
        else:
            print self.invalid
            return True

    def checkout(self):
        print('Which table do you want to check out?')
        choice = int(raw_input('>> '))
        if choice > 0 and choice <= 12:
            self.tables.tables[choice - 1].checkout()
        else:
            print(self.invalid)

    def checkin(self):
        print('Which table is checking in?')
        choice = int(raw_input('>> '))
        if choice > 0 and choice < 12:
            print(self.tables.checkin(choice - 1))
        else:
            print(self.invalid)

    def run(self):
        print "What is today's hourly rate?"
        self.tables.cost = float(raw_input('>> '))
        self.tables.view_tables()
        print self.prompt
        while self.choice(raw_input('>> ')):
            print self.line
            print self.prompt
            print self.line
        self.tables.dump(self.filename)

App()
