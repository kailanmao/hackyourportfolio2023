import tkinter as tk

def handle_input():
    for text_box in text_boxes:
        user_input = text_box.get("1.0", tk.END)
        print("User input:", user_input)
        # Do something with the user input

# Create the main Tkinter window
window = tk.Tk()

# Create a label for the title
title_label = tk.Label(window, text="Game Title")
title_label.pack()

# Create a list to hold the text boxes
text_boxes = []

# Create multiple Text widgets for text input
for i in range(3):
    text_box = tk.Text(window, height=5, width=30)
    text_box.pack()
    text_boxes.append(text_box)

# Create a button to handle the user input
button = tk.Button(window, text="Submit", command=handle_input)
button.pack()

# Start the Tkinter event loop
window.mainloop()
