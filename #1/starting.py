import random

# Generate a random integer between 1 and 2
random_number = random.randint(1, 2)

# Ask the user for input and convert it to an integer
user_input = int(input("Please enter a number (1 or 2): "))

# Compare the user input with the random number
if user_input == random_number:
    print("You win")
else:
    print("You lose")
    print("The number was:", random_number)