import os


class editDistance():
    def __init__(self, str1 = "pelican", str2 = "politician"):
        self.str1 = str1.lower()
        self.str2 = str2.lower()
        self.list = []

    def update(self, str1, str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()

    def printList(self):
        n = len(self.str1)+1
        m = len(self.str2)+1
        for j in range(m):
            for i in range(n):
                print(self.list[i][j], end=",")
                print(" ", end="")
            print()

    def solve(self):
        # n is the row, m is columns
        # want to go from left to right then down each row.
        n = len(self.str1)+1
        m = len(self.str2)+1
        dynamlist = [[0 for i in range(m)] for j in range(n)]
        #O(n)
        for i in range(n):
            dynamlist[i][0] = i

        #O(m)
        for j in range(m):
            dynamlist[0][j] = j

        #O(n*m)
        for i in range(1,n):
            for j in range(1,m):
                if self.str1[i-1] != self.str2[j-1]:
                    dynamlist[i][j] = min ([1 + dynamlist[i-1][j], 1+ dynamlist[i][j-1], 1 + dynamlist[i-1][j-1]])
                else:
                    dynamlist[i][j] = min ([1 + dynamlist[i-1][j], 1+ dynamlist[i][j-1], dynamlist[i-1][j-1]])

        self.list= dynamlist
        return dynamlist[n-1][m-1]


if __name__ == "__main__":
    test = editDistance("BARACKOBAMA", "KAMALAHARRIS")
    print(test.str1)
    print(test.str2)
    print(test.solve())
    test.printList()
