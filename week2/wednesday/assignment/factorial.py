def factorial(num):
    result = num
    if num == 0:
        result = 1
    for i in range(1,num):
        result *= i
    return result
