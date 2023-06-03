from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def get_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    
    # Load the selected image
    image = Image.open(file_path)
    
    # Create a Tkinter-compatible image
    image_tk = ImageTk.PhotoImage(image)
    
    # Update the image label
    return image_tk

# Create the Tkinter window
window = tk.Tk()

# Create an "Open Image" button
button = tk.Button(window, text="Open Image", command=open_image)
button.pack()

# Create an initial label (before an image is selected)
label = tk.Label(window)
label.pack()

# Start the Tkinter event loop
window.mainloop()