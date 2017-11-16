#ask user for name to delete
names = ["Alex","John","Mary","Seinfeld","Steve"]

print(names)
# index = -1
search = raw_input("Enter a name to be deleted: ")

# for i in range(0,len(names)):
#     if names[i].lower() == search.lower():
#         index = i
#     # print names[i]

### same thing with break
for i in range(0,len(names)):
    if names[i].lower() == search.lower():
        del names[i]
        break
    elif i == len(names)-1:
        print("Name not found")

# if index > 0:
#     del names[index]
# else:
#     print("Name not found")

print("The new array")
print(names)

# if nameToDolete in names:
#   print("Name is found")
