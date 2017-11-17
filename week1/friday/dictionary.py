# create a dictionary of all the numbers up to input with their squares

dict = {}
for i in range(0,int(raw_input("Enter an integral number: "))):
    dict[i] = i*i

print(dict)
