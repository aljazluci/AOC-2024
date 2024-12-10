
def countHashtags(board):
    sm = 0
    for row in board:
        sm += row.count('X')
    return sm

def checkAll(board, starting):
    sm = 0
    board[starting[0]][starting[1]] = '.'
    for i in range(len(board)):
        print(((i / len(board)) * 100) // 1, "%")
        for j in range(len(board[1])):
            if board[i][j] == '#' or (i, j) == starting:
                continue
            board[i][j] = '#'
            if checkLoop(board, starting):
                sm += 1
            board[i][j] = '.'
    return sm

def checkLoop(board, starting):
    ind = starting
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    deltaI = 0
    turnMap = dict()
    while True:
        new_row = ind[0] + deltas[deltaI][0]
        new_col = ind[1] + deltas[deltaI][1]
        if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
            return False
        if board[ind[0] + deltas[deltaI][0]][ind[1] + deltas[deltaI][1]] == '#':
            if ind in turnMap:
                if deltaI in turnMap[ind]:
                    return True
                turnMap[ind].append(deltaI)
            else:
                turnMap[ind] = [deltaI]
            deltaI = (deltaI + 1) % 4
        else: 
            ind = (new_row, new_col)

def findStarting(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '^':
                return (i, j)
    print("No start found")
    return None

def makePath(board, starting):
    ind = starting
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    deltaI = 0
    while True:
        board[ind[0]][ind[1]] = 'X'
        if (ind[0] + deltas[deltaI][0] >= len(board)) or (ind[1] + deltas[deltaI][1] >= len(board[0])):
            break
        if (ind[0] + deltas[deltaI][0] < 0) or (ind[1] + deltas[deltaI][1] < 0):
            break
        if board[ind[0] + deltas[deltaI][0]][ind[1] + deltas[deltaI][1]] == '#':
            deltaI = (deltaI + 1) % 4
        ind = (ind[0] + deltas[deltaI][0], ind[1] + deltas[deltaI][1])
        

def firstPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    makePath(board, findStarting(board))
    print(countHashtags(board))
    
def secondPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    print(checkAll(board, findStarting(board)))
    

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")