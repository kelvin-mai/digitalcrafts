# user_data = raw_input("Enter temperature in Celsius. ")
#
# print("You've entered " + user_data)
#
# convert_temp = float(user_data) * 1.8 + 32
#
# print("That temperature in Fahrenheit is {0}").format(convert_temp)

def celsius_to_fahrenheit(temp):
    return float(temp * 1.8 + 32)

def fahrenheit_to_celsius(temp):
    return float((temp-32) * 0.556)

# print("35C is {0}").format(celsius_to_fahrenheit(35))
# print("50F is {0}").format(fahrenheit_to_celsius(50))

def display_conversionCF(temp1):
    print("You've entered {0}".format(temp1))
    temp2 = celsius_to_fahrenheit(temp1)
    print("{0}C is {1}F".format(temp1, temp2))

def display_conversionFC(temp1):
    print("You've entered {0}".format(temp1))
    temp2 = fahrenheit_to_celsius(temp1)
    print("{0}F is {1}".format(temp1, temp2))
