import datetime
import os
import json
from pool_table import PoolTable
from pool_table import Tables

tables = Tables()
filename = datetime.date.today().strftime('%m-%d-%Y') + '.json'
if os.path.isfile(filename):
    tables.load(filename)
else:
    for i in range(12):
        tables.add_table(i)

print('---Pool table management app---')
tables.view_tables()
print('What is todays hourly rate?')
tables.cost = float(raw_input('>> '))
while True:
    print('---------------------------')
    print("'1' to checkout table")
    print("'2' to check in")
    print("'3' to view tables")
    print("'4' to quit")
    choice = raw_input('>> ')
    if choice == '1':
        print('Which table do you want to check out?')
        choice = int(raw_input('>> '))
        if choice > 0 and choice <= 12:
            tables.tables[choice - 1].checkout()
        else:
            print('Value out of range')
    elif choice == '2':
        print('Which table is checking in?')
        choice = int(raw_input('>> '))
        if choice > 0 and choice < 12:
            tables.checkin(choice - 1)
        else:
            print('Value out of range')
    elif choice == '3':
        tables.view_tables()
    elif choice == '4':
        break
    else:
        print('Invalid command! Try again.')

    print('---------------------------')

tables.view_tables()
tables.dump(filename)
