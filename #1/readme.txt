# Random Number Guessing Game

This is a simple Python script that generates a random number between 1 and 2, asks the user to input a number, and then compares the user's input with the generated random number to determine if the user wins or loses.

## How It Works

1. The script generates a random integer between 1 and 2.
2. The user is prompted to enter a number (1 or 2).
3. The script compares the user's input with the generated random number.
4. If the user's input matches the random number, the script prints "You win".
5. If the user's input does not match the random number, the script prints "You lose" and reveals the generated random number.

## Code

```python
import random

random_number = random.randint(1, 2)

# Ask the user for input and convert it to an integer
user_input = int(input("Please enter a number (1 or 2): "))

# Compare the user input with the random number
if user_input == random_number:
    print("You win")
else:
    print("You lose")
    print("The number was:", random_number)
```
## How to Run
Save the script in a file named starting.py.
Open a terminal and navigate to the directory containing starting.py.
Run the script using the following command:
Follow the on-screen instructions to enter a number and see if you win or lose.
## Requirements
Python 3.x