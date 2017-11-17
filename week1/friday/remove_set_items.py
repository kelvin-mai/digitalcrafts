#given these two arrays
names = ["Alex", "Mary", "Steve", "John", "Seinfeld", "Alan", "Jane"]
names_to_remove = ["Steve", "Alan"]

print(names)
print(names_to_remove)

set_names = set(names)
set_names_to_remove = set(names_to_remove)

set_names -= set_names_to_remove

#question asks us to return an array
names = list(set_names)


print(set_names)
print(names)
