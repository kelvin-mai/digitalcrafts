names = ["Alex", "Mary", "Steve", "John", "Seinfeld", "Alan", "Jane"]
namesToRemove = ["Steve", "Alan"]

print(names)
print(namesToRemove)

# def remove_item(arr, item):


for name in namesToRemove:
    # remove_item(names,name)
    for i in range(0,len(names)):
        if names[i] == name:
            del names[i]
            break

print(names)

# for x
#     for y
#         if namestodelete[x] == names[y]
