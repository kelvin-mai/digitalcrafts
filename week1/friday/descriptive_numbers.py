tens = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}
ones = {
    0: "",
    1: "One",
    2: "Two",
    3: "Tree",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
special_cases = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    100: "One Hundred"
}
# don't forget about the teens
while True:
    try:
        value = int(raw_input("Enter a number between 1 and 100: "))
    except ValueError:
        print("That was an invalid number!")

    if value > 0 and value <= 100:
        print("That value is linquistically represented by: ")
        if value < 10:
            print(ones[value])
        elif value >= 10 and value < 13:
            print(special_cases[value])
        elif value >= 13 and value < 20:
            print(ones[int(str(value)[1])] + "teen")
        elif value < 100 and value > 10:
            print(tens[int(str(value)[0])] + "-" + ones[int(str(value)[1])])
        elif value == 100:
            print("One Hundred")
    else:
        print("That was an invalid number!")

    if raw_input("Press any key to continue or q to quit: ").lower() == "q":
        break
