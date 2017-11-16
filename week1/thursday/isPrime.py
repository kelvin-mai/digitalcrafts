def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for x in range(2,num):
        if num % x == 0:
            return False
    return True

print("I check for prime numbers!")
if isPrime(int(raw_input("Enter a number: "))):
    print("That's a prime number!")
else:
    print("That's not prime!")
