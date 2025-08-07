import tkinter as tk
# def on_button_click():
#     print("Button Clicked!")

# window=tk.Tk()
# window.title("My First GUI App")
# window.geometry("400x300")

# label = tk.Label(window, text="Hello, Tkinter!")
# # label.pack()
# label.place(x=50, y=100) 
# button = tk.Button(window, text="Click Me",command=on_button_click)
# # button.pack()
# entry = tk.Entry(window)
# # entry.pack()
# print(entry.get())
# # label.grid(row=0, column=5)
# # button.grid(row=1, column=0)
# window.mainloop()

# Function to display text entered by user
def display_text():
    user_text = entry.get() # Get text from entry
    label.config(text=f"Hello, {user_text}!") # Update label text
# Create the main window
window = tk.Tk()
window.title("Simple Tkinter App")
window.geometry("400x200")# Create label, entry, and button
label = tk.Label(window, text="Enter your name:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Submit",command=display_text)
button.pack()
# Start the Tkinter event loop
window.mainloop()
