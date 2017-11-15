def even_or_odd(val):
    if val % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Even or odd?")
print(even_or_odd(int(raw_input("Enter a value: "))))
