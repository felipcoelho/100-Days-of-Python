#create a password generator
import random


letters_size = int(input("How many letters would you like in your password?\n"))
symbols_size = int(input("How many symbols would you like?\n"))
numbers_size = int(input("How many numbers would you like?\n"))

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()-+'
numbers = '0123456789'

password = ''
for _ in range(letters_size):
    password += random.choice(letters)
for _ in range(symbols_size):
    password += random.choice(symbols)
for _ in range(numbers_size):
    password += random.choice(numbers)


password = ''.join(random.sample(password, len(password)))  # Shuffle the password

print(f"Your generated password is: {password}")