import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if digit_var.get():
            characters += string.digits

        if special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = []

        
        if upper_var.get():
            password.append(random.choice(string.ascii_uppercase))

        if lower_var.get():
            password.append(random.choice(string.ascii_lowercase))

        if digit_var.get():
            password.append(random.choice(string.digits))

        if special_var.get():
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)

        final_password = ''.join(password)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid length")



def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first")



root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("450x400")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)


length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")


upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=digit_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=40)


generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="lightgreen"
)
generate_btn.pack(pady=15)


password_entry = tk.Entry(root, width=40, font=("Arial", 12))
password_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password,
    bg="lightblue"
)
copy_btn.pack()

root.mainloop()
