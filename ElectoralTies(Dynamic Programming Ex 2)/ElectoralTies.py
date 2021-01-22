import os
import pandas as pd

class electoralTies():
    def __init__(self, array, num):
        self.electoralvotes = array
        self.states = num
    def compute(self):
        n = int(self.states + 1)
        # m is number to tie
        m = int((sum(self.electoralvotes)/2) + 1)
        ties = [[0 for i in range(m)] for j in range(n)]

        # also handle edge case for tie at ties[0][0] = 1
        for i in range(n):
            ties[i][0] = 1
        for i in range(1,m):
            ties[0][i] = 0

        #how to handle dp problems: loop through items then loop condition
            # ex: states then number of votes for tie
        for j in range(1,n):
            for b in range(1,m):
                # array of electoralvotes is 0-50 (we are indexing 1 to 51)
                if self.electoralvotes[j-1] > b:
                    ties[j][b] = ties[j-1][b]
                else:
                    #ET[j,b] = ET[j-1,b - e[j]] + ET[j-1, b]
                    ties[j][b] = ties[j-1][b - self.electoralvotes[j-1]] + ties[j-1][b]
                    #print(self.electoralvotes[j-1], ties[j][b], j, b)

        #dynamically programmed through all states to get ties on m
        return ties[n-1][m-1]




if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\PC\OneDrive\Desktop\CSE101\HW6_electoral_votes.csv')
    array = df['Evs'].tolist()
    n = len(array)
    test = electoralTies(array, n)
    print(test.compute())

    test2 = electoralTies([3,4,4,5,6,8], 6)
    print(test2.compute())
