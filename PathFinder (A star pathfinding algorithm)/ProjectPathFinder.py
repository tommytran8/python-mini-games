import sys
import math
import tkinter as tk
from tkinter import *
import random as rd
class aStarNode():
    def __init__(self, x, y, randwalls = 0):
        self.x = x
        self.y = y
        self.gvalue = sys.maxsize
        self.hvalue = 0
        self.fvalue = sys.maxsize
        self.neighbors = []
        self.previous = None
        self.wall = False
        #set around 40 percent of grid to be random walls
        if randwalls == 1:
            rand = rd.randrange(0,10)
            if (rand == 1 or rand == 2 or rand == 3 or rand == 4):
                self.makewall()
    def makewall(self):
        self.wall = True
    def addneighbors(self, grid, col, row):
        xpos = self.x
        ypos = self.y
        if ypos < col-1:
            self.neighbors.append(grid[ypos + 1][xpos])
        if ypos > 0:
            self.neighbors.append(grid[ypos - 1][xpos])
        if xpos < row-1:
            self.neighbors.append(grid[ypos][xpos+1])
        if xpos > 0:
            self.neighbors.append(grid[ypos][xpos - 1])
        if ypos > 0 and xpos > 0:
            self.neighbors.append(grid[ypos -1][xpos - 1])
        if ypos < col-1 and xpos < row-1:
            self.neighbors.append(grid[ypos +1][xpos + 1])
        if ypos < col-1 and xpos > 0:
            self.neighbors.append(grid[ypos + 1][xpos - 1])
        if ypos > 0 and xpos < row -1:
            self.neighbors.append(grid[ypos -1][xpos + 1])
    def heuristic(self, end):
        #Euclidian distance
        #c = Sqrt(a^2 + b^2) => h = Sqrt((current_cell.x – goal.x)^2 + (current_cell.y – goal.y)^2 ) 
        return math.dist((self.x, self.y), (end.x, end.y))

class PathFinder():
    def __init__(self, col, row, randwalls= 1, startx = 0, starty=0, endx=24, endy=24):
        self.col = col
        self.row = row
        self.grid = [ [aStarNode(x = i, y= j, randwalls = randwalls) for i in range(col)] for j in range(row)]
        #Open List and Closed List (just like Dijkstra Algorithm)
        self.openset = []
        self.closedset = []
        self.path = []
        self.start = self.grid[starty][startx]
        self.start.gvalue = 0
        if endx == 24 and endy == 24:
            endx = col - 1
            endy = row - 1
        self.end = self.grid[endy][endx]
        self.setNeighbors()


    def setNeighbors(self):
        for y in range(self.row):
            for x in range(self.col):
                self.grid[x][y].addneighbors(self.grid, self.col, self.row)

    def findpath(self, h, w):
        if len(self.openset) > 0:
            lowestindex = 0
            #can use a priority queue here for openset
            for i,node in enumerate(self.openset):
                if (node.fvalue < self.openset[lowestindex].fvalue):
                    lowestindex = i
            tempnode = self.openset[lowestindex]
            #stops here if at end point
            if tempnode == self.end:
                temp = self.end
                while temp != None:
                    self.path.append(temp)
                    temp = temp.previous
                print("Successful Path!")
                self.openset.remove(tempnode)
                self.closedset.append(tempnode)
                #visualization of the result
                for node in self.openset:
                    tk.Frame(root,height= h/self.row,width= w/self.col, bg="green").grid(row = node.y, column= node.x)
                for node in self.closedset:
                    tk.Frame(root,height= h/self.row,width= w/self.col, bg="red").grid(row = node.y, column= node.x)
                for node in self.path:
                    tk.Frame(root,height= h/self.row,width= w/self.col, bg="blue").grid(row = node.y, column= node.x)
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.start.y, column= self.start.x)
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.end.y, column= self.end.x)
                return True
                
            else:
                #remove from list of nodes to be visited to list of already visited nodes
                self.openset.remove(tempnode)
                self.closedset.append(tempnode)

                for neighbor in tempnode.neighbors:
                    #only adds new nodes (neighbors of current node) if not wall and not already visited 
                    if neighbor not in self.closedset and not neighbor.wall:
                        #only update gvalue if new distance is better than current gvalue of neighbor nodes
                        if tempnode.gvalue + 1 < neighbor.gvalue:
                            neighbor.gvalue = tempnode.gvalue + 1
                            neighbor.hvalue = neighbor.heuristic(self.end)
                            neighbor.fvalue = neighbor.gvalue + neighbor.hvalue
                            neighbor.previous = tempnode
                            #adds new nodes if not in list
                            if neighbor not in self.openset:
                                self.openset.append(neighbor)
        else:
            #list of nodes to be visited is empty, so no solution
            print("No Solution")
            #visualization of result
            for node in self.openset:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="green").grid(row = node.y, column= node.x)
            for node in self.closedset:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="red").grid(row = node.y, column= node.x)
            for node in self.path:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="blue").grid(row = node.y, column= node.x)
            tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.start.y, column= self.start.x)
            tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.end.y, column= self.end.x)
            return True

        #checks for visual steps, if 1, visualize every step of PathFinder, if 0, only visualize result
        if (check2.get() == 1):
            for node in self.openset:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="green").grid(row = node.y, column= node.x)
            for node in self.closedset:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="red").grid(row = node.y, column= node.x)
            for node in self.path:
                tk.Frame(root,height= h/self.row,width= w/self.col, bg="blue").grid(row = node.y, column= node.x)
            tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.start.y, column= self.start.x)
            tk.Frame(root,height= h/self.row,width= w/self.col, bg="orange").grid(row = self.end.y, column= self.end.x)
        return False

def startup():
    global startwindow
    global walls
    global v1
    global v2
    global v3
    global v4
    startwindow.destroy()
    col = 25
    row = 25
    test = PathFinder(col, row, randwalls= check1.get(), startx =v1.get(), starty= v2.get(), endx = v3.get(), endy = v4.get())
    h = 500
    w = 500
    walls = {}

    if (check3.get() == 1):
        makeManuWalls(test)
    runPathFinder(test, h ,w, col, row)

#called in startup() method if user checked the manual walls box
def makeManuWalls(inp):
    global widget
    global walls
    #maybe change this to onDrag event
    def onClick(event):
        #the widget that gets clicked will turn into a wall (black box)
        event.widget.config(background = "black")
        inp.grid[test[event.widget][0]][test[event.widget][1]].wall = True

    #will open a new window where you can create the walls
    widget = tk.Tk()
    col = 25
    row = 25
    h= 500
    w= 500
    widget.config(height= h, width=w)  
    widget.resizable(False, False)
    widget.title("Exit to submit walls")
    test = {}
    for i in range(row):
        for j in range(col):
                if ((inp.start.y == i and inp.start.x == j) or (inp.end.y == i and inp.end.x == j)):
                    frame = tk.Frame(widget,height= h/row,width= w/col, bg="orange")
                elif inp.grid[i][j].wall == True:
                    frame = tk.Frame(widget,height= h/row,width= w/col, bg="black")
                
                else:
                    frame = tk.Frame(widget,height= h/row,width= w/col, bg="white")
                frame.grid(row = i, column= j)
                test[frame] = [i,j]

    widget.bind('<Button-1>', onClick)           
    widget.mainloop()
    
#called at end of startup() method
def runPathFinder(test, h , w, col, row):
    global root
    root = tk.Tk()
    root.title("PathFinder")
    #start and end should not be walls
    test.start.wall = False
    test.end.wall = False

    #sets up visualization of grid
    for i in range(row):
        for j in range(col):
            if ((test.start.y == i and test.start.x == j) or (test.end.y == i and test.end.x == j)):
                tk.Frame(root,height= h/row,width= w/col, bg="orange")
            elif (test.grid[i][j].wall == True):
                tk.Frame(root,height= h/row,width= w/col, bg="black").grid(row = i, column= j)
            else:
                tk.Frame(root,height= h/row,width= w/col, bg="white").grid(row = i, column= j)
    test.openset = []
    test.closedset = []
    #starts of the PathFinder algorithm with start point
    test.openset.append(test.start)
    while(test.findpath(h,w) != True):
        #this loop allows for visualization of every step
        root.update_idletasks()
        root.update()
    root.mainloop()

if __name__ == "__main__":
    
    #main(), where GUI is set up and called
    root = None
    widget = None
    walls = None
    startwindow = tk.Tk()
    startwindow.title("SetUp")

    #random walls, visual steps and manual walls checkbox
    check1 = tk.IntVar(startwindow, value = 1)
    check2 = tk.IntVar(startwindow, value = 0)
    check3 = tk.IntVar(startwindow, value = 0)

    #start and end points
    v1 = tk.IntVar(startwindow, value = 0)
    v2 = tk.IntVar(startwindow, value = 0)
    v3 = tk.IntVar(startwindow, value = 24)
    v4 = tk.IntVar(startwindow, value = 24)
    label1 = tk.Label(startwindow, text= "Enter start x cord").grid(row = 0, column = 0)
    entry1 = tk.Entry(startwindow, textvariable = v1).grid(row = 0, column= 1)
    label2 = tk.Label(startwindow, text= "Enter start y cord").grid(row = 1, column = 0)
    entry2 = tk.Entry(startwindow, textvariable = v2).grid(row = 1, column= 1)
    label3 = tk.Label(startwindow, text= "Enter end x cord").grid(row = 2, column = 0)
    entry3 = tk.Entry(startwindow, textvariable = v3).grid(row = 2, column= 1)
    label4 = tk.Label(startwindow, text= "Enter end y cord").grid(row = 3, column = 0)
    entry4 = tk.Entry(startwindow, textvariable = v4).grid(row = 3, column= 1)
    c1 = tk.Checkbutton(startwindow, text='Random Walls?', variable=check1, onvalue=1, offvalue=0,).grid(row = 4, column = 0)
    c2 = tk.Checkbutton(startwindow, text='Visual Steps?', variable=check2, onvalue=1, offvalue=0,).grid(row = 4, column = 1)
    c3 = tk.Checkbutton(startwindow, text='Manual Walls?', variable=check3, onvalue=1, offvalue=0,).grid(row = 5, column = 0)

    validLabel = tk.Label(startwindow, text= "Valid cordinate values: 0-24").grid(row = 6, column = 0)
    submitbutton = tk.Button(startwindow, text="Start PathFinder", padx=5, pady=5, fg="white", bg="black",command= startup).grid(row = 6, column= 1)
    startwindow.mainloop()
    
