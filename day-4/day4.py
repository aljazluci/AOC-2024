
def findX(board):
    arr = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                arr.append((i, j))
    return arr

def countXmas(board, ind):
    linePlus = [1,2,3]
    letters = ['M', 'A', 'S']
    lineMinus = [-1,-2,-3]
    lineZero = [0,0,0]
    cnt = 0
    ways = [(linePlus, lineMinus), (lineMinus, linePlus), (lineMinus, lineZero), 
            (linePlus, lineZero), (lineZero, lineMinus), (lineZero, linePlus),
            (linePlus, linePlus), (lineMinus, lineMinus)]
    for w in ways:
        try:
            for i, ws in enumerate(zip(w[0],w[1])):
                ii = ws[0]
                jj = ws[1]
                if ind[0] + ii < 0 or ind[1] + jj < 0:
                    raise Exception()
                if board[ind[0] +ii][ind[1] + jj] != letters[i]:
                    raise Exception()
            cnt += 1
        except:
            continue
    return cnt
    

def firstPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    print( sum([countXmas(board, i) for i in findX(board)]))
    
def windowCompare(boardPiece, window):
    # print(len(boardPiece), len(boardPiece[0]))
    for i in range(len(boardPiece)):
        for j in range(len(boardPiece[0])):
            # print(i, j)
            if window[i][j] == '.':
                continue
            if window[i][j] != boardPiece[i][j]:
                return False
    return True
    
def slidingWindow(board, window):
    cnt = 0
    for i in range(len(board) - len(window) + 1):
        for j in range(len(board[0]) - len(window[0]) + 1):
            if windowCompare([row[j:j+len(window[0])] for row in board[i:i+len(window)]], window):
                cnt +=1
    return cnt
    
def secondPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    windows = [[['M','.','M'],['.','A','.'],['S','.','S']], [['M','.','S'],['.','A','.'],['M','.','S']],
               [['S','.','S'],['.','A','.'],['M','.','M']], [['S','.','M'],['.','A','.'],['S','.','M']]]
    print(sum([slidingWindow(board, window) for window in windows]))
            
if __name__ == "__main__":
    # firstPart("input.txt")
    secondPart("input.txt")