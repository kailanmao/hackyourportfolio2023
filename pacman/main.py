from cmu_112_graphics import *
from maze import *
from pacman import *
from ghost import *
from bigDot import *
from dot import *

def appStarted(app):
    # game things
    app.timerDelay = 20
    app.score = 0
    app.lives = 3
    app.gameOver = False
    app.time = 0
    app.stateStartTime = 0
    app.pause = False
    app.lostLifeStartTime = 0

    # CHANGE LATER - STARTING GHOST STATE
    # app.ghostState = "frightened"

    # maze 2D list
    mazeList = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                 # row 2
                [2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
                 # row 3
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                 # row 4
                [2,2,2,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,
                 1,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,1,
                 1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,
                 1,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,1,
                 0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2],
                 # row 5
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                 # row 6
                [2,2,2,1,1,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,1,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
                 # row 7
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                 # row 8
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2],
                 # row 9
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                 # row 10
                [2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2],
                 # row 11
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                 # row 12
                [2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
                 1,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,1,
                 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
                 1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,
                 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2],

                 # row 11
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
                 # row 10
                [2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        
                 # row 9
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            
                 # row 8
                [2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
    
                 # row 7
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                 # row 6
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,1,1,1,1,1,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,1,1,1,1,1,1,2,2,2],
                 # row 5
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,
                 1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,1,
                 0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2],
                 # row 4
                [2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,
                 1,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,1,
                 0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,
                 1,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,1,
                 1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,2,2,2],
                 # row 3
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                [2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,1,0,1,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2,1,0,1,2,2,2],
                 # row 2
                [2,2,2,1,0,1,1,1,1,1,0,1,2,2,2,1,0,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,0,1,2,2,2,1,0,1,1,1,1,1,0,1,2,2,2],
                [2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2],
                [2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                 1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2],
                 # row 1
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
                ]
    app.maze = maze(mazeList, app)

    # pac man
    pacmanColor = 'yellow'
    pacmanR = 40
    pacmanC = 34
    app.pacman = pacman(pacmanColor, pacmanR, pacmanC, "Down")

    # ghosts
    app.ghost1 = ghost('red', 31, 34, 256)
    app.ghost2 = ghost('pink', 34, 34, 512)
    app.ghost3 = ghost('cyan', 34, 28, 128)
    app.ghost4 = ghost('orange', 34, 40, 16)
    app.ghosts = [app.ghost1, app.ghost2, app.ghost3, app.ghost4]

    # big dots
    app.bigDots = []
    app.bigDotPositions = [(10,10),(10,58),(58,10),(58,58)]
    for r, c in app.bigDotPositions:
        app.bigDots.append(bigDot(r, c))
    # dots
    app.dots = []
    app.dotPositions = []
    ghostHousePositions = [(31,34),(34,34),(34,28),(34,40),
                            (34,31),(34,37)]
    for r in range(4,len(app.maze.mazeList),3):
        for c in range(4,len(app.maze.mazeList[0]),3):
            if (app.maze.mazeList[r][c] == 0 and 
                (r,c) not in app.bigDotPositions and
                (r,c) not in ghostHousePositions):
                app.dots.append(dot(r, c))
                app.dotPositions.append((r, c))





def redrawAll(app, canvas):
    # maze - must go first
    app.maze.drawMaze(canvas)

    # score
    canvas.create_text(50, 15, text= f'Score: {app.score}',
                       fill='white', font='Helvetica 20 bold', anchor='w')

    # lives
    for i in range(1,app.lives*3,3):
        x0, y0, x1, y1 = app.maze.getCellBounds(67, i)
        d = x1 - x0
        canvas.create_oval(x0-d+2,y0-d+2,x1+d-2,y1+d-2,fill="yellow")

    # dots and bigDots
    for dot in app.dots:
        dot.drawDot(app,canvas)
    for bigDot in app.bigDots:
        bigDot.drawBigDot(app,canvas)

    # pacman and ghosts
    app.pacman.drawPacman(app, canvas)
    # pacman mouth animation
    if app.time % 3 == 0:
        app.pacman.drawPacmanMouth(app, canvas)

    for ghost in app.ghosts:
        ghost.drawGhost(app, canvas)
    
    # game over screen
    if app.gameOver:
        x0 = app.width // 2 - 200
        y0 = app.height // 2 - 100
        x1 = app.width // 2 + 200
        y1 = app.height // 2 + 100
        canvas.create_rectangle(x0,y0,x1,y1,fill="gold", outline="white")
        if len(app.dots) == 0 and len(app.bigDots) == 0:
            canvas.create_text(app.width // 2, app.height // 2,
            text="YOU WIN\nPress space to play again", fill="green",
            font="Helvetica 30 bold")
        else:
            canvas.create_text(app.width // 2, app.height // 2,
            text="YOU LOSE\nPress space to play again", fill="red3",
            font="Helvetica 30 bold")

def keyPressed(app, event):
    # start over game
    if app.gameOver and event.key == "Space":
        app.lives = 3
        app.score = 0
        app.gameOver = False
        app.time = 0
        app.stateStartTime = 0
        app.pause = False
        app.lostLifeStartTime = 0
        # big dots
        app.bigDots = []
        app.bigDotPositions = [(10,10),(10,58),(58,10),(58,58)]
        for r, c in app.bigDotPositions:
            app.bigDots.append(bigDot(r, c))
        # dots
        app.dots = []
        app.dotPositions = []
        ghostHousePositions = [(31,34),(34,34),(34,28),(34,40),
                                (34,31),(34,37)]
        for r in range(4,len(app.maze.mazeList),3):
            for c in range(4,len(app.maze.mazeList[0]),3):
                if (app.maze.mazeList[r][c] == 0 and 
                    (r,c) not in app.bigDotPositions and
                    (r,c) not in ghostHousePositions):
                    app.dots.append(dot(r, c))
                    app.dotPositions.append((r, c))
        # ghosts 
        for i in range(len(app.ghosts)):
            app.ghosts[i].color = app.ghosts[i].ghostColors[i]
            app.ghosts[i].r, app.ghosts[i].c = app.ghosts[i].startingPositions[i]
            app.ghosts[i].state = "chase"
        
        # pac man
        app.pacman.r = 40
        app.pacman.c = 34

    if event.key == app.pacman.direction:
        pass
    elif (event.key != "Space" and event.key != "Up" and event.key != "Down"
            and event.key != "Left" and event.key != "Right"):
        pass
    else:
        app.pacman.changeDirection(app, event.key)

def timerFired(app):
    app.time += 1
    if app.time - app.lostLifeStartTime == 10 and app.lostLifeStartTime != 0:
        app.pause = False
        app.pacman.r = 40
        app.pacman.c = 34
        app.pacman.direction = "Up"
        for i in range(len(app.ghosts)):
            r, c = app.ghosts[i].startingPositions[i]
            app.ghosts[i].r = r
            app.ghosts[i].c = c

    if app.time - app.stateStartTime == 200 and app.stateStartTime != 0:
        for i in range(len(app.ghosts)):
            if app.ghosts[i].state == "frightened":
                app.ghosts[i].state = "chase"
                app.ghosts[i].color = app.ghosts[i].ghostColors[i]

    # MUST GO AFTER TIME CHECKS
    if app.gameOver or app.pause:
        return

    # move pac-man
    app.pacman.move(app)

    # move ghosts
    for ghost in app.ghosts:
        if ghost.state == "frightened":
            ghost.path = []
            ghost.frightenedMove(app)
        else:
            if len(ghost.path) == 0:
                ghost.path = ghost.backtrack(app)
            elif app.time % ghost.timeInterval == 0 and (app.pacman.r, app.pacman.c) != ghost.path[-1]:
                ghost.path = ghost.backtrack(app)
            ghost.r, ghost.c = ghost.path[0]
            ghost.path.pop(0)


    # BIG DOT update score and game state
    if (app.pacman.r, app.pacman.c) in app.bigDotPositions:
        app.bigDotPositions.remove((app.pacman.r, app.pacman.c))
        app.bigDots.remove(bigDot(app.pacman.r, app.pacman.c))
        app.score += 50
        app.stateStartTime = app.time
        for ghost in app.ghosts:
            ghost.state = "frightened"
            ghost.color = "royal blue"
            ghost.path = []
    
    # SMALL DOT update score
    if (app.pacman.r, app.pacman.c) in app.dotPositions:
        app.dotPositions.remove((app.pacman.r, app.pacman.c))
        app.dots.remove(dot(app.pacman.r, app.pacman.c))
        app.score += 10
    
    # contact with ghosts
    for ghost in app.ghosts:
        nextR, nextC = ghost.getNextMove()
        if ((ghost.r == app.pacman.r and ghost.c == app.pacman.c) or
            (nextR == app.pacman.r and nextC == app.pacman.c)):
            if ghost.color == "royal blue":
                app.score += 200
                ghost.state = "chase"
                # return to normal color and go back to ghost house
                ghostNum = app.ghosts.index(ghost)
                ghost.color = ghost.ghostColors[ghostNum]
                ghost.r, ghost.c = ghost.startingPositions[ghostNum]
            else:
                app.lives -= 1
                for i in range(len(app.ghosts)):
                    app.ghosts[i].color = app.ghosts[i].ghostColors[i]
                    app.ghosts[i].r, app.ghosts[i].c = app.ghosts[i].startingPositions[i]
                    app.ghosts[i].path = []
                app.pause = True
                app.lostLifeStartTime = app.time

    # gameOver conditions
    # win
    if len(app.bigDots) == 0 and len(app.dots) == 0:
        app.gameOver = True
    # lose
    elif app.lives == 0:
        app.gameOver = True

runApp(width=600,height=600)