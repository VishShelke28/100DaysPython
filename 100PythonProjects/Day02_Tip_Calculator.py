# Program to calculate tip

print("Welcome to TIP Calculator!")

total_bill = float(input("What was the total bill? INR "))
tip = int(input("How much percentage you want to give tip? 10, 12 or 15? "))
people = int(input("Total bill will be divided in how many people? "))

bill_with_tip = total_bill + (total_bill *(tip/100))

# Python round() function float point number from the decimal value to the closest multiple of 10.
# The int value to the closest multiple of 10 to the power minus ndigits,
# where ndigits is the precision after the decimal point.
# If two multiples are equally close, rounding is done toward the even choice.

contribution_per_person = round((bill_with_tip / people))

print("Contribution per person : ", contribution_per_person)