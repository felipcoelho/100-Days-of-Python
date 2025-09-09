##################################################################### rollercoaster of life #####################################################################
# #greetings from the rollercoaster of life
# print("Welcome to the rollercoaster!")  
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



# # #odd or even
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")



# #greetings from the rollercoaster of life
# print("Welcome to the rollercoaster!")  
# # Ask the user to input their height
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     # Ask the user to input their age
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



##################################################################### BMI Calculator with Interpretations #####################################################################
# """
# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"
# """
# print("Welcome to the BMI Calculator!")
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# else:
#     print(f"Your BMI is {bmi}, you are overweight.")





##################################################################### rollercoaster of life #####################################################################
# #greetings from the rollercoaster of life
# print("Welcome to the rollercoaster!")  
# # Ask the user to input their height
# height = int(input("What is your height in cm? "))
# # Calculate the total bill
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     # Ask the user to input their age
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Child tickets are $5.")
#         bill = 5
#     elif age <= 18:
#         print("Teen tickets are $7.")
#         bill = 7
#     else:
#         print("Adult tickets are $12.")
#         bill = 12

#     # Ask the user if they want a photo taken
#     wants_photo = input("Do you want a photo taken? Y or N. ")

#     if wants_photo == "Y":
#         print("Your photo will be taken.")
#         bill += 3
#     else:
#         print("No photo will be taken.")

#     print(f"Your total bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



##################################################################### pizza delivery service #####################################################################
# #greetings from the pizza delivery service
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n")
# add_pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("Invalid size selected.")
#     exit()

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}.")



#################################################################### rollercoaster of life midlife crisis #####################################################################
#greetings from the rollercoaster of life
print("Welcome to the rollercoaster!")  
# Ask the user to input their height
height = int(input("What is your height in cm? "))
# Calculate the total bill
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    # Ask the user to input their age
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Teen tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12

    # Ask the user if they want a photo taken
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        print("Your photo will be taken.")
        bill += 3
    else:
        print("No photo will be taken.")

    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")