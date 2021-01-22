#GUI for my ProjectSudoku module
import tkinter as tk
from tkinter import *
import ProjectSudoku as su
import os
import random as rd
from copy import copy, deepcopy

#Loads the games from file
allGames = [[[0 for k in range(9)] for j in range(9)] for i in range(50)]
grid = [ [0] * 9 for _ in range(9)]
copygrid = [ [0] * 9 for _ in range(9)]
entries = [ [0] * 9 for _ in range(9)]
temp = ""
if os.path.isfile('listofSudokuGames.txt'):
    with open('listofSudokuGames.txt', 'r') as savefile:
        temp = savefile.read()
        temp = temp.split('\n')
for i in range(50):
    for j in range(81):
        allGames[i][int(j/9)][j%9] = int(temp[i][j])

root = tk.Tk()
    
canvas = tk.Canvas(root, height=800, width=700, bg="grey")
canvas.pack()

text = StringVar()
gameLabel = tk.Label(root, height = 1, textvariable=text, font=('Verdana',15))
gameLabel.pack()
text.set("Select New Game")
def resetgrid():
    global grid
    global copygrid
    for i in range(9):
        for j in range(9):
            copygrid[i][j] = grid[i][j]

#Starts the game with random game from list
def loadRandomGame():
    global allGames
    global grid
    global copygrid
    global entries
    global text
    choice = rd.randrange(0,50)
    text.set("Game " + str(choice + 1) + " Selected")
    grid = deepcopy(allGames[choice])
    copygrid = deepcopy(allGames[choice])
    entries = deepcopy(allGames[choice])
    resetBoard()


#creating/clearing sudoku board frame
def resetBoard():
    global entries
    global grid
    resetgrid()
    width=.1
    height=.085
    x=.01
    y=.01
    for i in range(9):
        for j in range(9):
            tk.Frame(root, bg ="white").place(relwidth=width, relheight=height, relx=x, rely=y)
            if (grid[i][j] != 0):
                tk.Label(root, text=grid[i][j], font=('Verdana',30)).place(relwidth=width, relheight=height, relx=x, rely=y)
            else:
                e= tk.Entry(root, font=('Verdana',30))
                e.place(relwidth=width, relheight=height, relx=x, rely=y)
                entries[i][j] = e
            x= x+.11   
        y = y + .095
        x = .01

    width=.01
    height=.845
    x=.33
    y=.01
    tk.Frame(root, bg ="black").place(relwidth=width, relheight=height, relx=x, rely=y)
    tk.Frame(root, bg ="black").place(relwidth=width, relheight=height, relx=x*2, rely=y)

    tk.Frame(root, bg ="black").place(relwidth=.98, relheight=.01, relx=.01, rely=.285)
    tk.Frame(root, bg ="black").place(relwidth=.98, relheight=.01, relx=.01, rely=.285*2)
#BOARD FRAME ENDS HERE

#User attempt submittions, and returns responses according to board state
def submit():
    global copygrid
    global entries
    global text
    #resets copygrid
    resetgrid()
    for i in range(9):
        for j in range(9):
            if (isinstance(entries[i][j], int)):
                #only instance int when entries was initialized
                copygrid[i][j] = entries[i][j]
                continue
            else:
                #checks entry object
                if (entries[i][j].get() == ""):
                    text.set("Empty boxes found, please complete the board before submitting")
                    break
                elif (not entries[i][j].get().isdigit() or int(entries[i][j].get()) > 9 or int(entries[i][j].get()) < 1):
                    text.set("Invalid Entry, please enter valid numbers (1-9)")
                    break
                else:
                    check = su.isValidNum(copygrid,i,j,int(entries[i][j].get()))
                    if check == False:
                        text.set("There are incorrect boxes, please try different inputs")
                        break
                    else:
                        #when valid entry, save to copygrid
                        copygrid[i][j] = int(entries[i][j].get())
        if (copygrid[i][j] == 0):
            #indicate there was a invalid box since loop broke out and didn't save a new value to copygrid[i][j]
            break
    if (su.findEmptyPos(copygrid, [0,0]) == False):
        #if grid is full, and no invalid entries
        text.set("Success!!")
        #redo board frame with solved board
        width=.1
        height=.085
        x=.01
        y=.01
        for i in range(9):
            for j in range(9):
                tk.Frame(root, bg ="white").place(relwidth=width, relheight=height, relx=x, rely=y)
                tk.Label(root, text=copygrid[i][j], font=('Verdana',30)).place(relwidth=width, relheight=height, relx=x, rely=y)
                x= x+.11
            y = y + .095
            x = .01
    


def solve():
    global copygrid
    global entries
    #get the answers
    resetgrid()
    su.solveSudoku(copygrid)
    for i in range(9):
        for j in range(9):
            entries[i][j] = copygrid[i][j]
    width=.1
    height=.085
    x=.01
    y=.01
    for i in range(9):
        for j in range(9):
            tk.Frame(root, bg ="white").place(relwidth=width, relheight=height, relx=x, rely=y)
            tk.Label(root, text=copygrid[i][j], font=('Verdana',30)).place(relwidth=width, relheight=height, relx=x, rely=y)
            x= x+.11
        y = y + .095
        x = .01

submitButton = tk.Button(root, text="Submit entries", padx=10, pady=5, fg="white", bg="black",
command=submit)
submitButton.place(x=550,y=735)

getSolutionButton = tk.Button(root, text="Get Solution", padx=10, pady=5, fg="white", bg="black",
command=solve)
getSolutionButton.place(x=375,y=735)

resetButton = tk.Button(root, text="Reset Board", padx=10, pady=5, fg="white", bg="black",
command=resetBoard)
resetButton.place(x=200,y=735)

newButton = tk.Button(root, text="New Game", padx=10, pady=5, fg="white", bg="black",
command=loadRandomGame)
newButton.place(x=25,y=735)

root.mainloop()
