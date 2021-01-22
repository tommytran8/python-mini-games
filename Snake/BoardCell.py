class Cell:
    def __init__(self, row, col, Ctype = 0):
        self.row = row
        self.col = col
        self.CellType = self.setCell(Ctype)
    def setCell(self, Ctype = 0):
        if (Ctype == 0):
            self.CellType = "Empty"
        elif (Ctype == 1):
            self.CellType = "Snake"
        else:
            self.CellType = "Bait"
