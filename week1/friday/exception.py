import calculator as calc

while True:
    while True:
        try:
            num1 = int(raw_input("Enter first number: "))
        except ValueError:
            print("Please enter valid value.")
            break

        try:
            num2 = int(raw_input("Enter second number: "))
        except ValueError:
            print("Please enter valid value.")
            break

        operand = raw_input("Enter operand: ")
        if operand == "+":
            print(calc.add(num1,num2))
        elif operand == "-":
            print(calc.subtract(num1,num2))
        elif operand == "*":
            print(calc.multiply(num1,num2))
        elif operand == "/":
            try:
                print(calc.divide(num1,num2))
            except ZeroDivisionError:
                print("Cannot divide by zero.")
        else:
            print("Invalid operand.")
        break

    if raw_input("Press any key to continue or q to quit: ").lower() == "q":
        break
