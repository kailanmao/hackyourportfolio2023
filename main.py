# helloGraphics.py VERSION 2.0
# from person import *
from cmu_112_graphics import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

class person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def drawPerson(self, app, canvas):
        canvas.create_polygon(self.x + 13, self.y + 13, self.x + 13,
                              self.y, self.x + 22, self.y,
                              fill='#939290', outline='#939290')

        # breathing
        t = app.time % 12
        # big
        if t <= 1 or t >= 10:
            canvas.create_polygon(self.x + 15, self.y + 15, self.x + 15,
                              self.y, self.x + 24, self.y,
                              fill='#828282', outline='#828282')
            canvas.create_rectangle(self.x - 15, self.y - 15, self.x + 15, self.y + 15,
                                    fill='#3389F8', outline='#3389F8')
            canvas.create_rectangle(self.x - 9, self.y - 6, self.x - 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
            canvas.create_rectangle(self.x + 9, self.y - 6, self.x + 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
        # medium
        elif t == 2 or t == 3 or t == 8 or t == 9:
            canvas.create_polygon(self.x + 14, self.y + 14, self.x + 14,
                              self.y, self.x + 23, self.y,
                              fill='#828282', outline='#828282')
            canvas.create_rectangle(self.x - 14, self.y - 14, self.x + 14, self.y + 15,
                                    fill='#3389F8', outline='#3389F8')
            canvas.create_rectangle(self.x - 8, self.y - 5, self.x - 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
            canvas.create_rectangle(self.x + 8, self.y - 5, self.x + 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
         # small
        else:
            canvas.create_polygon(self.x + 13, self.y + 13, self.x + 13,
                              self.y, self.x + 22, self.y,
                              fill='#828282', outline='#828282')
            canvas.create_rectangle(self.x - 13, self.y - 13, self.x + 13, self.y + 15,
                                    fill='#3389F8', outline='#3389F8')
            canvas.create_rectangle(self.x - 7, self.y - 4, self.x - 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
            canvas.create_rectangle(self.x + 7, self.y - 4, self.x + 4, self.y + 2,
                                fill='#A1E3FF', outline='#A1E3FF')
        
        # eyes
        # canvas.create_rectangle(self.x - 6, self.y - 3, self.x - 4, self.y + 2,
        #                         fill='#A1E3FF', outline='#A1E3FF')




def appStarted(app):
    app.state = "MENU"
    app.player = person(480, 440)
    app.time = 0
    app.timerDelay = 300
    app.nearGallery = False
    app.nearLibrary = False

    app.image1 = ''
    app.image2 = ''
    app.image3 = ''
    app.image4 = ''
    pass





def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 960, 720, fill='#AFA2FF') # light purple
    if app.state == "VIEW-OUTSIDE":
        # back to menu
        canvas.create_rectangle(20, 20, 120, 60, fill='#7043EB', outline='#7043EB')
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 12', fill='#f0f0f0')

        # grass
        canvas.create_rectangle(177, 107, 784, 614, fill='#AFA2FF', outline='#7043EB', width=5)
        canvas.create_rectangle(180, 110, 780, 610, fill='#17B890', outline='#17B890')
        # path
        canvas.create_rectangle(460, 450, 500, 612, fill='#E6CA97', outline='#E6CA97')
        canvas.create_polygon(460, 450, 500, 450, 320, 300, 280, 300, fill='#E6CA97', outline='#E6CA97')
        canvas.create_polygon(460, 450, 500, 450, 680, 300, 640, 300, fill='#E6CA97', outline='#E6CA97')

        # gallery
        canvas.create_polygon(370, 300, 370, 260, 410, 260, fill='#297D50', outline='#297D50')
        canvas.create_rectangle(230, 200, 370, 300, fill='#A97C72', outline='#A97C72')
        canvas.create_rectangle(220, 190, 380, 220, fill='#76473D', outline='#76473D')
        canvas.create_text(300, 205, text='GALLERY', font='Helvetica 18 bold', fill='#f0f0f0')
        canvas.create_arc(320, 300, 280, 250, fill='#4C3122', outline='#4C3122', style='pieslice',
                          extent=180)
        canvas.create_rectangle(280, 275, 320, 300, fill='#4C3122', outline='#4C3122')
        canvas.create_oval(285, 280, 290, 285, fill='#FAE480', outline='#FAE480')

        if app.nearGallery:
            canvas.create_text(480, 70, text='Press Space to Enter Gallery', fill='#7043EB',
                               font="Helvetica 30")
        elif app.nearLibrary:
            canvas.create_text(480, 70, text='Press Space to Enter Library', fill='#7043EB',
                               font="Helvetica 30")
        else:
            app.nearGallery = False
            app.nearLibrary = False


        # library
        # canvas.create_line(640, 300, 680, 300, fill='red')
        canvas.create_polygon(720, 300, 720, 260, 760, 260, fill='#297D50', outline='#297D50')
        canvas.create_rectangle(600,220,720,300,fill='#F3EDD3',outline='#F3EDD3')
        canvas.create_polygon(660,180,580,230,740,230,fill='#B60808',outline='#B60808')
        canvas.create_text(660, 220, text='LIBRARY', font='Helvetica 18 bold', fill='#f0f0f0')
        canvas.create_polygon(599,240,599,270,570,270,fill='#B60808',outline='#B60808')
        canvas.create_rectangle(570,270,599,300,fill='#C6C1AC',outline='#C6C1AC')
        canvas.create_rectangle(640, 260, 680, 300, fill='#A97C72', outline='#A97C72')
        


        # player
        app.player.drawPerson(app, canvas)



    elif app.state == "MENU":
        canvas.create_rectangle(177, 107, 784, 614, fill='#AFA2FF', outline='#7043EB', width=5)

        canvas.create_text(485, 225, text="'U'niverse", font="Helvetica 60 bold",
                           fill="#5A5A5A")
        canvas.create_text(480, 220, text="'U'niverse", font="Helvetica 60 bold",
                           fill="#f0f0f0")
        canvas.create_text(app.width/2, 280, text="Revolutionary way of showing your life highlights. It's all about U!",
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
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 12', fill='#f0f0f0')

        # upload images
        canvas.create_text(170, 180, text='Upload Images', font='Helvetica 20', fill='#7043eb')
        canvas.create_text(170, 210, text='(e.g. pictures of projects, events, awards)', font='Helvetica 15', fill='#f0f0f0')

        if app.image1 == '':
            canvas.create_rectangle(400, 160, 480, 200, fill='#7043EB', outline='#7043EB')
        else:
            canvas.create_rectangle(400, 160, 480, 200, fill='#8A5FFF', outline='#7043EB', width=2)
        
        if app.image2 == '':
            canvas.create_rectangle(530, 160, 610, 200, fill='#7043EB', outline='#7043EB')
        else:
            canvas.create_rectangle(530, 160, 610, 200, fill='#8A5FFF', outline='#7043EB', width=2)

        if app.image3 == '':
            canvas.create_rectangle(660, 160, 740, 200, fill='#7043EB', outline='#7043EB')
        else:
            canvas.create_rectangle(660, 160, 740, 200, fill='#8A5FFF', outline='#7043EB', width=2)
        
        if app.image4 == '':
            canvas.create_rectangle(790, 160, 870, 200, fill='#7043EB', outline='#7043EB')
        else:
            canvas.create_rectangle(790, 160, 870, 200, fill='#8A5FFF', outline='#7043EB', width=2)
        

        canvas.create_text(440, 180, text='Image 1', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(570, 180, text='Image 2', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(700, 180, text='Image 3', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(830, 180, text='Image 4', font='Helvetica 13', fill='#f0f0f0')

        # upload files
        canvas.create_text(170, 380, text='Upload Files', font='Helvetica 20', fill='#7043eb')
        canvas.create_text(170, 410, text='(e.g. your resume, research, writing samples)', font='Helvetica 15', fill='#f0f0f0')
        
        canvas.create_rectangle(400, 360, 480, 400, fill='#7043EB', outline='#7043EB')
        canvas.create_rectangle(530, 360, 610, 400, fill='#7043EB', outline='#7043EB')
        canvas.create_rectangle(660, 360, 740, 400, fill='#7043EB', outline='#7043EB')
        canvas.create_rectangle(790, 360, 870, 400, fill='#7043EB', outline='#7043EB')

        canvas.create_text(440, 380, text='File 1', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(570, 380, text='File 2', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(700, 380, text='File 3', font='Helvetica 13', fill='#f0f0f0')
        canvas.create_text(830, 380, text='File 4', font='Helvetica 13', fill='#f0f0f0')

    elif app.state == "VIEW-GALLERY":
        canvas.create_rectangle(177, 107, 784, 614, fill='#AFA2FF', outline='#7043EB', width=5)
        # back to menu
        canvas.create_rectangle(20, 20, 120, 60, fill='#7043EB', outline='#7043EB')
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 12', fill='#f0f0f0')

        # back to portfolio (<)
        canvas.create_text(480, 70, text='Press Space to Return to Portfolio', fill='#7043EB',
                               font="Helvetica 30")

        # gallery
        image1 = Image.open("default.jpg")
        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test, bg='#7043EB')
        label1.image = test
        # Position image
        label1.place(x=180, y=110)

    elif app.state == "VIEW-LIBRARY":
        canvas.create_rectangle(177, 107, 784, 614, fill='#AFA2FF', outline='#7043EB', width=5)
        # back to menu
        canvas.create_rectangle(20, 20, 120, 60, fill='#7043EB', outline='#7043EB')
        canvas.create_text(70, 40, text='Back to Menu', font='Helvetica 12', fill='#f0f0f0')

        canvas.create_text(480, 70, text='Press Space to Return to Portfolio', fill='#7043EB',
                               font="Helvetica 30")

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
    elif app.state == "VIEW-OUTSIDE" or app.state == "VIEW-LIBRARY" or app.state == "VIEW-GALLERY":
        # back to menu
        if event.x >= 20 and event.x <= 120 and event.y >= 20 and event.y <= 60:
            app.state = "MENU"
    elif app.state == "CREATE":
        # back to menu
        if event.x >= 20 and event.x <= 120 and event.y >= 20 and event.y <= 60:
            app.state = "MENU"
        # upload images
        elif event.y >= 160 and event.y <= 200:
            if event.x >= 400 and event.x <= 480:
                app.image1 = get_image()
            elif event.x >= 530 and event.x <= 610:
                app.image2 = get_image()
            elif event.x >= 660 and event.x <= 740:
                app.image3 = get_image()
            elif event.x >= 790 and event.x <= 870:
                app.image4 = get_image()



def keyPressed(app, event):
    if app.state == "VIEW-LIBRARY":
        # print("in\n")
        if event.key == 'Space':
            # print("double in\n")
            app.state = "VIEW-OUTSIDE"
    elif app.state == "VIEW-GALLERY":
        if event.key == 'Space':
            app.state = "VIEW-OUTSIDE"
    elif app.state == "VIEW-OUTSIDE":
        if event.key == "Up":
            if app.player.y > 125:
                app.player.y -= 10
        elif event.key == "Down":
            if app.player.y < 595:
                app.player.y += 10
        elif event.key == "Left":
            if app.player.x > 195:
                app.player.x -= 10
        elif event.key == "Right":
            if app.player.x < 765:
                app.player.x += 10
        elif event.key == "Space":
            if app.nearGallery:
                app.state = "VIEW-GALLERY"
            elif app.nearLibrary:
                app.state = "VIEW-LIBRARY"
    else:
        pass



def get_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    
    # Load the selected image
    # image = Image.open(file_path)
    
    # Create a Tkinter-compatible image
    # image_tk = ImageTk.PhotoImage(image)
    
    # Update the image label
    return file_path



def timerFired(app):
    # print(f"x: {app.player.x}, y: {app.player.y}\n")
    print(f"state: {app.state}")
    app.time += 4
    if (app.player.x >= 210 and app.player.x <= 390
        and app.player.y >= 180 and app.player.y <= 320):
        app.nearGallery = True
    elif (app.player.x >= 580 and app.player.x <= 700 and
            app.player.y >= 200 and app.player.y <= 320):
        app.nearLibrary = True
    else:
        app.nearGallery = False
        app.nearLibrary = False

runApp(width=960, height=720) 