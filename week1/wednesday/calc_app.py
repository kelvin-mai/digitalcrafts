import calculator as calc

print("Enter a math problem with (+,-,*,/)")
num1 = int(raw_input())
operator = raw_input()
num2 = int(raw_input())

if operator == "+":
    print(calc.add(num1,num2))
elif operator == "-":
    print(calc.subtract(num1,num2))
elif operator == "*":
    print(calc.multiply(num1,num2))
elif operator == "/":
    print(calc.divide(num1,num2))
else:
    print("Sorry, that wasn't a valid expression. Good bye!")
