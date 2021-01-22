#need to make this a class and make my methods private, i.e def __printgrid(grid). Make everything private except solveSudoku()

def printgrid(grid):
    for row in range(9):
        for col in range(9):
            print(str(grid[row][col]), end=" ")
        print('\n')

def findEmptyPos(grid, pos):
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                pos[0] = row
                pos[1]= col
                return True
    return False

#helper method for isValidNum
def validInBox(grid, row, col, num):
    rowlist = [0,3,6,9]
    collist = [0,3,6,9]
    checkrow = 0
    checkcol = 0

    #checks in a specific box
    for i in range(3):
        if (row >= rowlist[i] and row < rowlist[i+1]):
            checkrow = rowlist[i]
    for i in range(3):
        if (col >= collist[i] and col < collist[i+1]):
            checkcol = collist[i]
    
    #checks if box contain num
    for i in range(checkrow,checkrow + 3):
        for j in range(checkcol, checkcol + 3):
            if (num == grid[i][j]):
                return False
    return True

#helper method for isValidNum
def validInRow(grid, row, num):
    if (num in grid[row]):
        return False
    return True

#helper method for isValidNum
def validInCol(grid, col, num):
    for row in range(9):
        if (num == grid[row][col]):
            return False
    return True

#checks if number is already in 3x3 box or row or col, if so, return False and check different number
def isValidNum(grid, row, col, num):
    return validInBox(grid, row, col, num) and validInRow(grid, row, num) and validInCol(grid, col, num)

#backtrace recursion, it will return a board that is filled with a completed sudoku board
def solveSudoku(grid):
    pos = [0,0]
    #using a list to pass in row and col by reference to get empty position in grid
    if (not findEmptyPos(grid, pos)):
        # if grid is filled, sudoku board is solved, success!!
        return True
    row = pos[0]
    col = pos[1]
    #checks for valid inputs to current position (row, col) and if it is ever invalid, it will backtrace through recursion
    #loops 9 times since there are 9 valid inputs (1-9)
    for num in range(1,10):
        if (isValidNum(grid,row,col,num)):
            grid[row][col] = num
            if (solveSudoku(grid)):
                #if False here, backtrace
                return True
            grid[row][col] = 0        
    return False


if __name__=="__main__":
    #need to make a function that can generate a playable sudoku board
    #or have a list of sudoku games saved in games.txt and use randomizer to choose game
    testgrid = [[3,0,6,5,0,8,4,0,0],
                [5,2,0,0,0,0,0,0,0],
                [0,8,7,0,0,0,0,3,1],
                [0,0,3,0,1,0,0,8,0],
                [9,0,0,8,6,3,0,0,5],
                [0,5,0,0,9,0,6,0,0],
                [1,3,0,0,0,0,2,5,0],
                [0,0,0,0,0,0,0,7,4],
                [0,0,5,2,0,6,3,0,0]]

    testgrid2 = [[8,0,0,0,0,0,0,0,0],
                [0,0,3,6,0,0,0,0,0],
                [0,7,0,0,9,0,2,0,0],
                [0,5,0,0,0,7,0,0,0],
                [0,0,0,0,4,5,7,0,0],
                [0,0,0,1,0,0,0,3,0],
                [0,0,1,0,0,0,0,6,8],
                [0,0,8,5,0,0,0,1,0],
                [0,9,0,0,0,0,4,0,0]]

    #since lists are mutable, I will change content of testgrid without having to return it
    solveSudoku(testgrid) # if function returns false, it is not a valid sudoku board
    solveSudoku(testgrid2)
    printgrid(testgrid)
    print("\nNEWLINE\n")
    printgrid(testgrid2)
