import sqlite3
import customtkinter
import time
import logging
import datetime

# Function to validate the date format
def validate_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to add a birthday to the database with retry mechanism
def add_birthday(name, birthdate):
    if not validate_date_format(birthdate):
        error_label.configure(text="Invalid date format. Please use YYYY-MM-DD.")
        error_label.grid()
        return

    retries = 10  # Increase number of retries
    delay = 2  # Increase delay between retries in seconds
    for attempt in range(retries):
        try:
            logging.debug(f"Attempt {attempt + 1} to add birthday: {name}, {birthdate}")
            conn = sqlite3.connect('data.db')  # Connect to the database
            conn.execute('PRAGMA journal_mode=WAL')  # Enable WAL mode
            c = conn.cursor()
            c.execute('INSERT INTO birthdays (name, birthdate) VALUES (?, ?)', (name, birthdate))  # Insert the new birthday
            conn.commit()
            conn.close()  
            update_birthdays_list()  # Update the list of birthdays displayed
            error_label.configure(text="")  # Clear the error message
            error_label.grid_remove()  # Remove the error label from the grid
            logging.debug("Birthday added successfully")
            break  # Exit the loop if the operation is successful
        except sqlite3.OperationalError as e:
            logging.error(f"OperationalError: {e}")
            if "database is locked" in str(e):
                time.sleep(delay)  # Wait before retrying
            else:
                raise  # Raise the exception if it's not a locking issue
    else:
        logging.error("Failed to add birthday after several retries")

# Function to retrieve all birthdays from the database
def get_birthdays():
    try:
        conn = sqlite3.connect('data.db')  # Connect to the database
        conn.execute('PRAGMA journal_mode=WAL')  # Enable WAL mode
        c = conn.cursor()
        c.execute('SELECT name, birthdate FROM birthdays ORDER BY birthdate desc')  # Retrieve all birthdays
        birthdays = c.fetchall()  # Fetch all results
        conn.close()
        return birthdays  # Return the list of birthdays
    except sqlite3.OperationalError as e:
        logging.error(f"OperationalError while fetching birthdays: {e}")
        return []

# Function to update the list of birthdays displayed in the textbox
def update_birthdays_list():
    birthdays = get_birthdays()  # Get the list of birthdays
    birthdays_text = "\n \n".join([f"{name}: {birthdate}" for name, birthdate in birthdays])  # Format the birthdays text
    textbox.configure(state='normal')  # Enable the textbox for editing
    textbox.delete("1.0", customtkinter.END)  # Clear the textbox
    textbox.insert(customtkinter.END, birthdays_text)  # Insert the formatted birthdays text
    textbox.configure(state='disabled')  # Disable the textbox to make it read-only

# Function to create the GUI
def create_gui():
    global textbox, error_label
    root = customtkinter.CTk()  # Initialize the main window
    root.title("Birthday Reminder")  # Set the window title

    frame = customtkinter.CTkFrame(master=root)  # Create a frame to hold the widgets
    frame.grid(pady=20, padx=60, sticky="nsew")  # Place the frame in the window

    label = customtkinter.CTkLabel(master=frame, text="Name:")  # Create a label for the name entry
    label.grid(row=0, column=0, pady=12, padx=12, sticky="w")  # Place the label in the frame

    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter name")
    entry.grid(row=0, column=1, pady=12, padx=12, sticky="ew")

    label2 = customtkinter.CTkLabel(master=frame, text="Birthdate:")
    label2.grid(row=1, column=0, pady=12, padx=12, sticky="w")

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="YYYY-MM-DD")
    entry2.grid(row=1, column=1, pady=12, padx=12, sticky="ew")

    button = customtkinter.CTkButton(master=frame, text="Add birthday", command=lambda: add_birthday(entry.get(), entry2.get()))
    button.grid(row=2, column=0, columnspan=2, pady=12, padx=12, sticky="ew")

    error_label = customtkinter.CTkLabel(master=frame, text="", text_color="red")  # Label for error messages
    error_label.grid(row=3, column=0, columnspan=2, pady=12, padx=12, sticky="ew")
    error_label.grid_remove()  # Initially remove the error label from the grid

    label3 = customtkinter.CTkLabel(master=frame, text="Upcoming Birthdays:")
    label3.grid(row=4, column=0, columnspan=2, pady=0, padx=12, sticky="w")

    textbox = customtkinter.CTkTextbox(master=frame, width=300, height=200)
    textbox.grid(row=5, column=0, columnspan=2, pady=12, padx=12, sticky="nsew")
    textbox.configure(state='disabled')

    update_birthdays_list()  # Update the list of birthdays when the GUI starts

    root.mainloop()

# Run the GUI
create_gui()