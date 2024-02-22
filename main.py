import tkinter as tk

def submit_form():
    # Retrieve data from input fields
   print("*")
    # Clear other fields similarly

# Create the main application window
root = tk.Tk()
root.title("Scholarship Form")
root.minsize(800,800)

# Create input fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Mobile No:").pack()
name1_entry = tk.Entry(root)
name1_entry.pack()

tk.Label(root, text="Class: ").pack()
name2_entry = tk.Entry(root)
name2_entry.pack()

tk.Label(root, text="Income: ").pack()
name3_entry = tk.Entry(root)
name3_entry.pack()

tk.Label(root, text="Education:").pack()
name4_entry = tk.Entry(root)
name4_entry.pack()


tk.Label(root, text="Email Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create other input fields similarly

# Submit button
submit_button = tk.Button(root, text="Submit")
submit_button.pack()

# Run the application
root.mainloop()
