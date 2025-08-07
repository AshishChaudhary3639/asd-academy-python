import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    selected_hobbies = [hobby_listbox.get(i) for i in hobby_listbox.curselection()]
    result = f"""
    Name: {name_var.get()}
    Gender: {gender_var.get()}
    Subscribe: {'Yes' if subscribe_var.get() else 'No'}
    Country: {country_var.get()}
    Age: {age_var.get()}
    Hobbies: {', '.join(selected_hobbies)}
    Comments: {comments_text.get("1.0", tk.END).strip()}
    """
    messagebox.showinfo("Form Submitted", result)

root = tk.Tk()
root.title("All Tkinter Widgets Demo")
root.geometry("600x700")

# Menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Files", menu=filemenu)
root.config(menu=menubar)

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar()
subscribe_var = tk.BooleanVar()
country_var = tk.StringVar()
age_var = tk.IntVar(value=25)

# Label & Entry
tk.Label(root, text="Name:").pack(anchor="w", padx=20, pady=2)
tk.Entry(root, textvariable=name_var, width=40).pack(padx=10)

# Radio Buttons
tk.Label(root, text="Gender:").pack(anchor="w", padx=10, pady=5)
genders = ["Male", "Female", "Other"]
for g in genders:
    tk.Radiobutton(root, text=g, variable=gender_var, value=g).pack(anchor="w", padx=20)

# Checkbutton
tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var).pack(anchor="w", padx=10, pady=5)

# Combobox
tk.Label(root, text="Country:").pack(anchor="w", padx=10, pady=5)
ttk.Combobox(root, textvariable=country_var, values=["USA", "UK", "India", "Australia"], state="readonly").pack(padx=10)

# Spinbox for Age
tk.Label(root, text="Age:").pack(anchor="w", padx=10, pady=5)
tk.Spinbox(root, from_=10, to=100, textvariable=age_var).pack(padx=10)

# Listbox for Hobbies
tk.Label(root, text="Hobbies (select multiple):").pack(anchor="w", padx=10, pady=5)
hobby_listbox = tk.Listbox(root, selectmode="multiple", height=4)
for hobby in ["Reading", "Gaming", "Traveling", "Music"]:
    hobby_listbox.insert(tk.END, hobby)
hobby_listbox.pack(padx=10)

# Slider (Scale)
tk.Label(root, text="Rate this form (1–10):").pack(anchor="w", padx=10, pady=5)
tk.Scale(root, from_=1, to=10, orient="horizontal").pack(padx=10)

# Text box
tk.Label(root, text="Additional Comments:").pack(anchor="w", padx=10, pady=5)
comments_text = tk.Text(root, height=5, width=50)
comments_text.pack(padx=10)

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()
