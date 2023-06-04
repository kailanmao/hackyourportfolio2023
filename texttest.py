import tkinter as tk

def handle_input():
    user_input = text.get("1.0", tk.END)
    print("User input:", user_input)
    # Do something with the user input

# Create the main Tkinter window
window = tk.Tk()

# Create a Text widget for multiline input
text = tk.Text(window, height=5, width=30)
text.pack()

# Create a button to handle the user input
button = tk.Button(window, text="Submit", command=handle_input)
button.pack()

# Start the Tkinter event loop
window.mainloop()

