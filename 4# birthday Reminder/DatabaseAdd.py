import sqlite3
import customtkinter

def add_birthday(name, birthdate):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO birthdays (name, birthdate) VALUES (?, ?)', (name, birthdate))
    conn.commit()
    conn.close()
    update_birthdays_list()

def get_birthdays():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT name, birthdate FROM birthdays ORDER BY birthdate desc')
    birthdays = c.fetchall()
    conn.close()
    return birthdays

def update_birthdays_list():
    birthdays = get_birthdays()
    birthdays_text = "\n ".join([f"{name}: {birthdate}" for name, birthdate in birthdays])
    textbox.configure(state='normal')
    textbox.delete("1.0", customtkinter.END)
    textbox.insert(customtkinter.END, birthdays_text)
    textbox.configure(state='disabled')

def create_gui():
    global textbox
    root = customtkinter.CTk()  # Initialize the main window
    root.title("Birthday Reminder")

    frame = customtkinter.CTkFrame(master=root)
    frame.grid(pady=20, padx=60, sticky="nsew")

    label = customtkinter.CTkLabel(master=frame, text="Name:")
    label.grid(row=0, column=0, pady=12, padx=12, sticky="w")

    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter name")
    entry.grid(row=0, column=1, pady=12, padx=12, sticky="ew")

    label2 = customtkinter.CTkLabel(master=frame, text="Birthdate:")
    label2.grid(row=1, column=0, pady=12, padx=12, sticky="w")

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter birthdate")
    entry2.grid(row=1, column=1, pady=12, padx=12, sticky="ew")

    button = customtkinter.CTkButton(master=frame, text="Add birthday", command=lambda: add_birthday(entry.get(), entry2.get()))
    button.grid(row=2, column=0, columnspan=2, pady=12, padx=12, sticky="ew")

    label3 = customtkinter.CTkLabel(master=frame, text="Upcoming Birthdays:")
    label3.grid(row=3, column=0, columnspan=2, pady=12, padx=12, sticky="w")

    textbox = customtkinter.CTkTextbox(master=frame, width=300, height=200)
    textbox.grid(row=4, column=0, columnspan=2, pady=50, padx=12, sticky="nsew")
    textbox.configure(state='disabled')

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(4, weight=1)

    update_birthdays_list()
    root.mainloop()

if __name__ == "__main__":
    create_gui()