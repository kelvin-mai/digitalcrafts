# with opens and closes automatically so you don't have to do it manually
filename = 'helloworld.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines :
        print(line.rstrip('\n'))

# writing a file
with open('filetowrite.txt','w') as file_object:
    file_object.write('Hello World, I am using Python to write you.')

# appending file
with open('filetowrite.txt', 'a') as file_object:
    file_object.write('\nBye World')
