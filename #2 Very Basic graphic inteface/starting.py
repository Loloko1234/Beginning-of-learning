import tkinter as tk
import random

def check_guess():
    try:
        user_input = int(entry.get())
        if user_input not in [1, 2]:
            result_label.config(text="Please enter a valid number (1 or 2).")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number (1 or 2).")
        return

    random_number = random.randint(1, 2)
    if user_input == random_number:
        result_label.config(text="You win!")
    else:
        result_label.config(text=f"You lose. The number was: {random_number}")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create and place the widgets
prompt_label = tk.Label(root, text="Please enter a number (1 or 2):")
prompt_label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()