import sys

def minimax(nodeInd, depth, isMaximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeInd]
    children = [nodeInd * 2, nodeInd* 2 + 1]
    if isMaximizingPlayer:
        best = -sys.maxsize
        for child in children:
            value = minimax(child, depth + 1, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = sys.maxsize
        for child in children:
            value = minimax(child, depth + 1, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
if __name__ == "__main__":
    #each values are a left node (tree of depth 3)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print(minimax(0,0,True,values, -sys.maxsize, sys.maxsize))