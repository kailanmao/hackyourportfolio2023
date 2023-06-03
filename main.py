# helloGraphics.py VERSION 2.0
from cmu_112_graphics import *
from tkinter import *
from PIL import Image, ImageTk
from person import *
from tkinter import filedialog

def appStarted(app):
    app.state = "MENU"
    app.player = person(480, 610)
    pass





def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 960, 720, fill='#AFA2FF') # light purple
    if app.state == "VIEW-OUTSIDE":
        # back to menu
        canvas.create_rectangle(20, 20, 120, 60, fill='#7043EB', outline='#7043EB')
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 15', fill='#f0f0f0')

        # grass
        canvas.create_rectangle(180, 110, 780, 610, fill='#17B890', outline='#17B890')
        # canvas.create_rectangle(240+180, 195+110, 360+180, 295+110, fill='#ffffff', outline='#ffffff')

    elif app.state == "MENU":
        canvas.create_text(app.width/2, 220, text='3D Portfolio', font="Helvetica 60 bold",
                           fill="#f0f0f0")
        canvas.create_text(app.width/2, 280, text='Create and explore your very own 3D portfolio!',
                           font='Helvetica 20', fill='#7043eb')
        
        # view
        canvas.create_rectangle(400, 320, 560, 400, fill='#7043eb', outline='#7043eb')
        canvas.create_text(app.width/2, 360, text='View', font="Helvetica 20", fill='#f0f0f0')

        # create
        canvas.create_rectangle(400, 420, 560, 500, fill='#7043eb', outline='#7043eb')
        canvas.create_text(app.width/2, 460, text='Create', font="Helvetica 20", fill='#f0f0f0')
        # canvas.create_rectangle()
    elif app.state == "CREATE":
        # back to menu
        canvas.create_rectangle(20, 20, 120, 60, fill='#7043EB', outline='#7043EB')
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 15', fill='#f0f0f0')
    else:
        pass
    
    # canvas.pack()
    # img = ImageTk.PhotoImage(Image.open("images/brownie-pixelart-2.png"))
    # canvas.create_image(20, 20, anchor=NW, image=img)



def mousePressed(app, event):
    if app.state == "MENU":  
        # view button
        if event.x >= 400 and event.x <= 560 and event.y >= 320 and event.y <= 400:
            app.state = "VIEW-OUTSIDE"

        # create button
        if event.x >= 400 and event.x <= 560 and event.y >= 420 and event.y <= 500:
            app.state = "CREATE"
    elif app.state == "VIEW-OUTSIDE":
        # back to menu
        if event.x >= 20 and event.x <= 120 and event.y >= 20 and event.y <= 60:
            app.state = "MENU"
    elif app.state == "CREATE":
        # back to menu
        if event.x >= 20 and event.x <= 120 and event.y >= 20 and event.y <= 60:
            app.state = "MENU"



def keyPressed(app, event):
    pass



def get_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    
    # Load the selected image
    image = Image.open(file_path)
    
    # Create a Tkinter-compatible image
    image_tk = ImageTk.PhotoImage(image)
    
    # Update the image label
    return image_tk




runApp(width=960, height=720) 