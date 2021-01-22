import sys 
import time 


class TicTacToe:
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.playerturn = 1
        self.winner = None
    def move(self, i, j):
        if (self.board[j][i] != 0):
            print("Please enter into VALID square")
            return 0
        elif (self.playerturn == 1):
            self.board[j][i] = 1
            self.playerturn = 2
        elif (self.playerturn == 2):
            self.board[j][i] = 2
            self.playerturn = 1
    def isFull(self):
        for j in range(3):
            for i in range(3):
                if (self.board[j][i] == 0):
                    return False
        return True
    def gameOver(self):
        isFull = self.isFull()
        for player in range(1,3):
            if (self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player):
                self.winner = player
                return True
            elif (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player):
                self.winner = player
                return True
            elif (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player):
                self.winner = player
                return True
            elif (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player):
                self.winner = player
                return True
            elif (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player):
                self.winner = player
                return True
            elif (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player):
                self.winner = player
                return True
            elif (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
                self.winner = player
                return True
            elif (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
                self.winner = player
                return True
        if (self.winner == None and isFull):
            #3 will indicate draw
            self.winner = 3
            return True
        if (self.winner == None and not isFull):
            return False
    def printBoard(self):
        for j in range(3):
            for i in range(3):
                print(self.board[j][i], end= " ")
            print("")
def readInput():
    print("It is player " + str(newGame.playerturn) + "'s turn.")
    x = input("Enter x cord ")
    y = input("Enter y cord ")
    return (x,y)
if __name__ == "__main__":
    newGame = TicTacToe()
    while (newGame.gameOver() == False):
        newGame.printBoard()
        (x, y) = readInput()
        newGame.move(int(x),int(y))

    newGame.printBoard()
    print("GameOver.")
    if (newGame.winner == 3):
        print("Draw")
    else:
        print("Winner is player: " + str(newGame.winner))