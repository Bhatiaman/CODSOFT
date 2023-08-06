import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters=""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Please select at least one option for the password."

    password = "".join(random.choices(characters, k=length))
    return password

def display_password(length_entry, uppercase_var, lowercase_var, digits_var, special_var, password_display):
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        password_display.config(text=f"Generated Password: {password}")
    except ValueError as e:
        password_display.config(text=str(e))

def create_gui():
    #create main window
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("450x250")
    
    #apply style
    style = ttk.Style()
    style.theme_use("clam")

    #create widgets
    label = ttk.Label(window, text="Enter Password Length:")
    label.pack(pady=10)

    length_entry = ttk.Entry(window)
    length_entry.pack()

    options_frame = ttk.Frame(window)
    options_frame.pack(pady=10)

    uppercase_var = tk.BooleanVar()
    uppercase_checkbox = ttk.Checkbutton(options_frame, text="Uppercase Letters", variable=uppercase_var)
    uppercase_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    lowercase_var = tk.BooleanVar()
    lowercase_checkbox = ttk.Checkbutton(options_frame, text="Lowercase Letters", variable=lowercase_var)
    lowercase_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    digits_var = tk.BooleanVar()
    digits_checkbox = ttk.Checkbutton(options_frame, text="Digits", variable=digits_var)
    digits_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    special_var = tk.BooleanVar()
    special_checkbox = ttk.Checkbutton(options_frame, text="Special Characters", variable=special_var)
    special_checkbox.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    password_display = ttk.Label(window, text="")
    password_display.pack()

    generate_button = ttk.Button(window, text="Generate Password", command=lambda: display_password(length_entry, uppercase_var, lowercase_var, digits_var, special_var, password_display))
    generate_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()