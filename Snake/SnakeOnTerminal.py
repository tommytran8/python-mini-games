import BoardCell as c
import LinkedList as lk
import random as rd
import string
import sys, time, msvcrt
class SnakeGame():
    def __init__(self, Snake):
        self.snake = Snake
        self.board = None
        self.gameOver = False
        self.direction = 1
        self.setUpBoard()

    def setUpBoard(self):
        #setup a 10x10 board, with a snake a (4,9) by default
        self.board = [[c.Cell(col = i, row = j,Ctype = 0) for i in range(10)] for j in range(10)]
        node = self.snake.head
        #adds snake to board
        while (node != None):
            self.board[node.cell.row][node.cell.col] = node.cell
            node = node.nextNode
        #adds a bait to board
        self.generateFood()

    def updateSnake(self, cell):
        #case for hitting wall when gameOver already set to True
        if cell == 0:
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
                #make tail the new head
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
        if row > 9 or col > 9 or row < 0 or col < 0:
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
        rand1 = rd.randrange(0,10)
        rand2 = rd.randrange(0,10)
        if (self.board[rand1][rand2].CellType != "Snake"):
            #can't be snake cell
            self.board[rand1][rand2].setCell(2)
        else:
            self.generateFood()

    def setDirection(self, direction):
        self.direction = direction

    #prints board
    def printBoard(self):
        for j in range(10):
            for i in range(10):
                if (self.board[j][i].CellType == "Snake"):
                    print("1", end =" ")
                elif (self.board[j][i].CellType == "Bait"):
                    print("2", end =" ")
                else:
                    print("*", end =" ")
            print('\n', end="")
    
def readInput(default, timeout = 0.3):
    #method to read user input every 0.5 seconds, if no or invalid input it will run the previous direction (default)
    start_time = time.time()
    input = 0
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 119:
                input = "w"
            elif ord(byte_arr) == 115: 
                input= "s"
            elif ord(byte_arr) == 100: 
                input= "d"
            elif ord(byte_arr) == 97:
                input= "a"
        if  (time.time() - start_time) > timeout:
            break
    #only allows valid inputs, if not use default
    print("")
    if input in inputs[default-1]:
        return input
    else:
        return default
if __name__ == "__main__":
    snake = lk.LinkedList()
    snake.head = lk.Node(c.Cell(row = 9, col = 4))
    snake.head.cell.setCell(1)
    newGame = SnakeGame(snake)
    #valid inputs based on current direction
    inputs = [["w", "s", "d"], ["a", "s", "d"], ["a", "s", "w"], ["a", "w", "d"] ]
    while newGame.gameOver != True:
        #loop to run snake game on terminal
        newGame.printBoard() 
        print("")
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
    print("Game Over!")