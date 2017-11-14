subtotal = float(raw_input("Enter total amount: "))
percentage = float(raw_input("Enter tip percentage: "))

tip = subtotal * (percentage / 100)

print "Your tip is " + str(tip)
