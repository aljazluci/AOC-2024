import functools

def findZeros(board):
    ret = []
    for i in range(len(board)):
        for j, b in enumerate(board[i]):
            if b == 0:
                ret.append((i, j))
    return ret

def checkValid(board, ind):
    return (0 <= ind[0] < len(board)) and (0 <= ind[1] < len(board[0]))

def findPath(board, ind):
    arr = []
    curr = board[ind[0]][ind[1]]
    if curr == 9:
        return [ind]
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    nextInds = [(ind[0] + delta[0], ind[1] + delta[1]) for delta in deltas]
    for nextInd in nextInds:
        if checkValid(board, nextInd):
            if board[nextInd[0]][nextInd[1]] - curr == 1:
                arr.extend(findPath(board, nextInd))
    return arr
                

def firstPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
        board = [[int(v) for v in l] for l in board]
    sm = 0
    for z in findZeros(board):
        sm += len(set(findPath(board, z)))
    print(sm)
    
def secondPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
        board = [[int(v) for v in l] for l in board]
    sm = 0
    for z in findZeros(board):
        sm += len(findPath(board, z))
    print(sm)

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")