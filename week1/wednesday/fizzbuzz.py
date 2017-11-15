def fizzbuzz(val):
    if val % 3 == 0 and val % 5:
        return "Fizz Buzz"
    elif val % 3 == 0:
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    else
        return "Nope!"

print("Let's play FizzBuzz!!")
print(fizzbuzz( int(raw_input("Enter a value:")) ))
