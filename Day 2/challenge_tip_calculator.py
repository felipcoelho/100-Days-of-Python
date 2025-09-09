# create a greeting for the user to the tip calculator program
print("Welcome to the tip calculator!")
# ask the user for the total bill
bill = float(input("What was the total bill? $"))
# ask the user how much tip they would like to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# ask the user how many people to split the bill
people = int(input("How many people to split the bill? "))
# calculate the total bill including tip
total_bill = bill + (bill * tip / 100)
# calculate the bill per person
bill_per_person = total_bill / people
# format the bill per person to 2 decimal places
bill_per_person = "{:.2f}".format(bill_per_person)
# print the final bill per person
print(f"Each person should pay: ${bill_per_person}")