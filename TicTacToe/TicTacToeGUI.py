import pygame
import sys 
import time 
from pygame.locals import *
import copy
pygame.init() 
player1image = pygame.image.load(r'C:\Users\PC\OneDrive\Desktop\Python Projects\TicTacToe\assets\o_modified-100x100.png') 
player2image = pygame.image.load(r'C:\Users\PC\OneDrive\Desktop\Python Projects\TicTacToe\assets\X_modified-100x100.png')
class TicTacToe:
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.playerturn = 1
        self.winner = None
        #allow 2 players if desired
        self.twoplayers = False
    def move(self, i, j):
        #user position obtained from userinput and update board
        if (self.board[j][i] != 0):
            #if try to check a filled square
            print("Please enter into VALID square")
            return 0
        elif (self.playerturn == 1):
            #player 1 turn
            self.board[j][i] = 1
            self.playerturn = 2
        elif (self.playerturn == 2):
            #player 2 turn
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
        #check all win conditions for each player
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
            #game continues
            return False
    def printBoard(self):
        #displays GUI after move for TicTacToe
        screen.fill((255,255,255))
        for j in range(3):
            for i in range(3):
                if (self.board[j][i] == 1):
                    screen.blit(player1image, (i * 100, j * 100))
                elif (self.board[j][i] == 2):
                    screen.blit(player2image, (i * 100, j * 100))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))
        pygame.display.update()

def readInput():
    #read GUI user input and gets position of move
    input1 = pygame.event.get()
    for event in input1:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return pygame.mouse.get_pos()
        if event.type == QUIT:
            return True
    return False

def AImove():
    def findAllEmptyPos(board):
        templist = []
        for j in range(3):
            for i in range(3):
                if (board[j][i] == 0):
                    templist.append((i,j))
        return templist
    #minimax algorithm
    def minimax(board, computer, playerturn, alpha= -sys.maxsize, beta= sys.maxsize):
        listempty = findAllEmptyPos(board)
        copyGame = TicTacToe()
        copyGame.board = board
        copyGame.playerturn = playerturn
        if copyGame.gameOver():
            if (copyGame.winner == 2):
                return 1
            elif (copyGame.winner == 1):
                return -1
            else:
                return 0
        if playerturn == computer: #maximazing AI
            best = -sys.maxsize
            for pos in listempty:
                board[pos[1]][pos[0]] = 2
                value = minimax(board, 2, 1, alpha, beta)
                board[pos[1]][pos[0]] = 0
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = sys.maxsize
            for pos in listempty:
                board[pos[1]][pos[0]] = 1
                value = minimax(board, 2, 2, alpha, beta)
                board[pos[1]][pos[0]] = 0
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best
    board = copy.deepcopy(newGame.board)
    possiblePos = findAllEmptyPos(board)
    bestScore = -sys.maxsize
    bestpos = None
    for pos in possiblePos:
        board[pos[1]][pos[0]] = 2
        score = minimax(board, 2, 1)
        board[pos[1]][pos[0]] = 0
        if score > bestScore:
            bestScore = score
            bestpos = pos
    return bestpos
if __name__ == "__main__":
    newGame = TicTacToe()
    screen = pygame.display.set_mode((300, 300)) 
    while (newGame.gameOver() == False):
        newGame.printBoard()
        #two players
        if newGame.twoplayers == True:
            pos = readInput() 
            #get pos of mouse: if return False, keep trying to read input, if return True, then player quited the game
            #else they clicked.
            if (pos == False):
                continue
            elif (pos == True):
                break
            x = int(pos[0] / 100)
            y = int(pos[1] / 100)
            newGame.move(int(x),int(y))
        
        #you vs AI
        else:
            #need to make it arbitrary, (1 or 2) for user and AI
            if newGame.playerturn == 1:
                pos = readInput()
                if (pos == False):
                    continue
                elif (pos == True):
                    break
                x = int(pos[0] / 100)
                y = int(pos[1] / 100)
                newGame.move(int(x),int(y))
            else:
                pos = AImove()
                print(pos)
                x = int(pos[0])
                y = int(pos[1])
                newGame.move(int(x),int(y))

    newGame.printBoard()
    print("GameOver.")
    if (newGame.winner == 3):
        #3 indicated as draw in gameOver()
        print("Draw")
    else:
        print("Winner is player: " + str(newGame.winner))


    #OPTIMIZE by making a menu, allows user to choose 2 players or vs AI. Allow user to choose which side he want to play (1 or 2).