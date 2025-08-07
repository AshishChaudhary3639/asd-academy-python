import tkinter as tk
from tkinter import ttk, messagebox
import openpyxl
import os

# Excel file setup
file_path = "test_data.xlsx"

if not os.path.exists(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Name", "Email", "Gender", "Country", "Subscribe"])
    workbook.save(file_path)

# Function to submit the form
def submit_form():
    name = name_var.get()
    email = email_var.get()
    gender = gender_var.get()
    country = country_var.get()
    subscribe = "YES" if subscribe_var.get() else "NO"

    if not name or not email or gender == "Select" or country == "Select":
        messagebox.showwarning("Validation Error", "Please fill all the required fields.")
        return

    # Append data to Excel file
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet.append([name, email, gender, country, subscribe])
    workbook.save(file_path)

    messagebox.showinfo("Success", "Form submitted successfully!")

    # Clear form
    name_var.set("")
    email_var.set("")
    gender_var.set("Select")
    country_var.set("Select")
    subscribe_var.set(False)

# Main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x400")
root.resizable(False, False)

# # Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar(value="Select")
country_var = tk.StringVar(value="Select")
subscribe_var = tk.BooleanVar()

# Labels and Inputs
tk.Label(root, text="Name *").pack(pady=5)
tk.Entry(root, textvariable=name_var, width=40).pack()

# tk.Label(root, text="Email *").pack(pady=5,anchor=tk.E,padx=20)
tk.Label(root, text="Email *").pack(pady=5)
tk.Entry(root, textvariable=email_var, width=40).pack()
# # tk.Entry(root, textvariable=email_var, width=40).pack(anchor=tk.W)

tk.Label(root, text="Gender *").pack(pady=5)
choices=["Male", "Female", "Other"]
ttk.Combobox(root, textvariable=gender_var, values=choices, state="readonly").pack()

# # tk.Label(root, text="Gender *").grid(row=0, column=0, padx=5, pady=5, sticky="w")
# # choices = ["Male", "Female", "Other"]
# # ttk.Combobox(root, textvariable=gender_var, values=choices, state="readonly").grid(row=0, column=1, padx=5, pady=5)


tk.Label(root, text="Country *").pack(pady=5)
ttk.Combobox(root, textvariable=country_var, values=["India", "USA", "UK", "Canada", "Other"], state="readonly").pack()

tk.Checkbutton(root, text="Subscribe to newsletter monthly", variable=subscribe_var).pack(pady=5)

tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white", width=20).pack(pady=20)

root.mainloop()
