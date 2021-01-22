import sys, time, msvcrt, os
import BoardCell as c
import LinkedList as lk
sys.stdout= open(os.devnull, 'w')
import pygame
import tkinter as tk
from pygame.locals import *
import random as rd
import string
sys.stdout = sys.__stdout__
class SnakeGame():
    def __init__(self, Snake, row = 10, col = 10):
        self.row = row
        self.col = col
        self.snake = Snake
        self.board = None
        self.gameOver = False
        self.direction = 1
        self.setUpBoard(row, col)

    def setUpBoard(self, row, col):
        #setup a 10x10 board, with a snake a (4,9) by default
        self.board = [[c.Cell(col = i, row = j,Ctype = 0) for i in range(col)] for j in range(row)]
        node = self.snake.head
        #adds snake to board
        while (node != None):
            self.board[node.cell.row][node.cell.col] = node.cell
            node = node.nextNode
        #adds a bait to board
        self.generateFood()

    def updateSnake(self, cell):
        #case for hitting wall when gameOver already set to True
        if self.gameOver == True:
            return 0
        #case for crashing into self, sets gameOver
        if cell.CellType == "Snake":
            node = self.snake.head
            #get end of snake
            while (node.nextNode != None and node.nextNode.cell.CellType != "Empty"):
                node = node.nextNode
            #if next cell is tail
            if node.cell is cell:
                node = self.snake.head
                while (node.nextNode.cell != cell):
                    node = node.nextNode
                #set tail as new head
                node.nextNode = None
                temp = self.snake.head
                newNode = lk.Node(cell)
                if (temp.cell.CellType != "Empty"):
                    newNode.nextNode = temp
                self.snake.head = newNode
            else:
                #set gameOver is hit snake part other than tail
                self.gameOver = True
            return 0
        #case for when cell is bait, then grow snake
        elif cell.CellType == "Bait":
            self.grow(cell)
            self.generateFood()
            return 0
        else:
            #when cell is a empty, can move to it. Update snake
            node = self.snake.head
            #get end of snake and set to empty
            while (node.nextNode != None and node.nextNode.cell.CellType != "Empty"):
                node = node.nextNode
            node.cell.setCell(0)
            #update on board
            self.board[node.cell.row][node.cell.col] = node.cell
            temp = self.snake.head
            #set new head of snake as input cell
            cell.setCell(1)
            newNode = lk.Node(cell)
            if (temp.cell.CellType != "Empty"):
                newNode.nextNode = temp
            self.snake.head = newNode
            return 0

    def nextCell(self):
        #gets next cell based on input direction
        col = self.snake.head.cell.col
        row = self.snake.head.cell.row
        if self.direction == 1:
            col += 1
        elif self.direction == 2:
            row += 1
        elif self.direction == 3:
            col -= 1
        elif self.direction == 4:
            row -=1
        #case when cell is wall, set gameOver to true
        if row > self.row-1 or col > self.col-1 or row < 0 or col < 0:
            self.gameOver = True
            return 0
        cell = self.board[row][col]
        return cell

    def grow(self, bait):
        #make bait cell as new snake head as 'growth'
        node = self.snake.head
        newNode = lk.Node(bait)
        newNode.cell.setCell(1)
        newNode.nextNode = node
        self.snake.head = newNode

    def generateFood(self):
        #randomize bait location
        rand1 = rd.randrange(0,self.row)
        rand2 = rd.randrange(0,self.col)
        if (self.board[rand1][rand2].CellType != "Snake"):
            #can't be snake cell
            self.board[rand1][rand2].setCell(2)
        else:
            self.generateFood()

    def setDirection(self, direction):
        self.direction = direction

    #display GUI Board
    def printBoard(self):
        screen.fill((255,255,255))
        for j in range(self.row):
            for i in range(self.col):
                if (self.board[j][i].CellType == "Snake"):
                    pygame.draw.rect(screen, (255, 0, 0), (self.board[j][i].col*vel, self.board[j][i].row*vel, vel, vel))
                elif (self.board[j][i].CellType == "Bait"):
                    pygame.draw.rect(screen, (0, 255, 0), (self.board[j][i].col*vel, self.board[j][i].row*vel, vel, vel))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (self.board[j][i].col*vel, self.board[j][i].row*vel, vel, vel))
        pygame.display.update()

def readInput(default):
    #method to read keyboard input to move snake or close game
    input1 = pygame.event.get()
    input = default
    pygame.time.delay(120)
    for event in input1:
        if event.type == KEYDOWN:
            if event.key == K_a:
                input = "a"
            if event.key == K_d:
                input = "d"
            if event.key == K_w:
                input = "w"
            if event.key == K_s:
                input = "s"
            if event.key == K_BACKSPACE:
                newGame.gameOver = True
        elif event.type == QUIT:
            newGame.gameOver = False
    if (len(input1) == 0):
        return default
    if input in inputs[default-1]:
        return input
    else:
        return default

def startup():
    #the function that makes the game
    global v1
    global v2
    global rowinp
    global colinp
    global newGame
    global screen
    root.destroy()
    rowinp = v1.get()
    colinp = v2.get()
    snake = lk.LinkedList()
    snake.head = lk.Node(c.Cell(row = 9, col = 4))
    snake.head.cell.setCell(1)
    newGame = SnakeGame(snake, row =rowinp, col =colinp)

    screen = pygame.display.set_mode((vel*colinp, vel*rowinp))
    while newGame.gameOver != True:
        #loop to run snake game on GUI
        newGame.printBoard()
        userinput = readInput(newGame.direction)
        if userinput == "d":
            if (newGame.direction != 3):
                newGame.setDirection(1)
        elif userinput == "s":
            if (newGame.direction != 4):
                newGame.setDirection(2)
        elif userinput == "a":
            if (newGame.direction != 1):
                newGame.setDirection(3)
        elif userinput == "w":
            if (newGame.direction != 2):
                newGame.setDirection(4)
        cell = newGame.nextCell()
        newGame.updateSnake(cell)
    print("Game Over!") #print gameover in a tkinter gui instead if want to optimize
    return 0

def menu():
    #menu to prompt user input and to start game
    global v1
    global v2
    global root
    root = tk.Tk()
    v1 = tk.IntVar(root, value = 10)
    v2 = tk.IntVar(root, value = 10)
    root.title("Enter grid size")
    root.geometry("250x80")
    label1 = tk.Label(root, text= "Enter row").grid(row = 0, column = 0)
    tk.Entry(root, textvariable = v1).grid(row = 0, column= 1)
    label2 = tk.Label(root, text= "Enter col").grid(row = 1, column = 0)
    tk.Entry(root, textvariable = v2).grid(row = 1, column= 1)
    #button will call startup()
    submitButton = tk.Button(root, text="Start Game", padx=10, pady=5, fg="white", bg="black",
    command=startup).grid(row = 2, column= 0)
    root.mainloop()

pygame.init()
if __name__ == "__main__":
    #THIS BLOCK CAN BE GLOBAL VARIABLE INSTEAD
    v1 = None
    v2 = None
    root = None
    rowinp = None
    colinp = None
    newGame = None
    screen = None
    vel = 30
    #valid inputs based on current direction
    inputs = [["w", "s", "d"], ["a", "s", "d"], ["a", "s", "w"], ["a", "w", "d"] ]
    #BLOCK END HERE

    menu()

    #OPIMIZE, MAKE METHOD AND VARIABLE MORE NEAT, ALSO MAKE A BETTER GUI AND BETTER MENU
