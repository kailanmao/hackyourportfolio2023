from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def open_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    print("THE FILE PATH:\n")
    print(file_path)
    
    # Load the selected image
    image = Image.open(file_path)
    print("THE IMAGE:\n")
    print(image)
    
    # Create a Tkinter-compatible image
    image_tk = ImageTk.PhotoImage(image)
    
    # Update the image label
    label.config(image=image_tk)
    label.image = image_tk
    return image

# Create the Tkinter window
window = tk.Tk()

# Create an "Open Image" button
button = tk.Button(window, text="open image", command=open_image)
button.pack()

# Create an initial label (before an image is selected)
label = tk.Label(window)
label.pack()

# Start the Tkinter event loop
window.mainloop()