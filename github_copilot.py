# Intentional errors in the code
def greet_user(name):
    print("Hello, " + name) # Missing colon in function definition

greet_user("Alice") # Missing closing parenthesis

for i in range(5): # Missing colon
    print("Number: " + str(i)) # Concatenating string with integer

my_list = [1, 2, 3, 4, 5]
print(my_list[10]) # IndexError: Accessing out-of-range index