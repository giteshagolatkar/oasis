from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"Your BMI is: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")



root = Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.config(bg="#dff6ff")


title_label = Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#dff6ff",
    fg="#003566"
)
title_label.pack(pady=20)


weight_label = Label(
    root,
    text="Enter Weight (kg):",
    font=("Arial", 12),
    bg="#dff6ff"
)
weight_label.pack()

weight_entry = Entry(root, font=("Arial", 12), width=25)
weight_entry.pack(pady=10)


height_label = Label(
    root,
    text="Enter Height (m):",
    font=("Arial", 12),
    bg="#dff6ff"
)
height_label.pack()

height_entry = Entry(root, font=("Arial", 12), width=25)
height_entry.pack(pady=10)


calc_button = Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#0077b6",
    fg="white",
    padx=10,
    pady=5,
    command=calculate_bmi
)
calc_button.pack(pady=20)


result_label = Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#dff6ff",
    fg="#000814"
)
result_label.pack(pady=10)


root.mainloop()
