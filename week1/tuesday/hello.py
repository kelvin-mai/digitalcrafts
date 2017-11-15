name = raw_input("What is your name? ")
age = raw_input("What is your age? ")

# message = name + age

# message = "My name is " + name + " and my age is " + age

message = "My name is {0} and my age is {1}".format(name, age) #string interpolation

print(message)
