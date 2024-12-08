def checkBounds(ind, board):
    return (0 <= ind[0] < len(board)) and (0 <= ind[1] < len(board[0]))

def makeDict(board):
    rt = dict()
    for i in range(len(board)):
        for j, c in enumerate(board[i]):
            if c == '.' or c == '#':
                continue
            if c in rt:
                rt[c].append((i, j))
            else:
                rt[c] = [(i, j)]
    return rt

def getAntinodes(ind1, ind2, board):
    base = ((ind1[0] - (ind1[0]- ind2[0])), ind1[1] - (ind1[1] - ind2[1]))
    diff = ((ind1[0] - ind2[0]), (ind1[1] - ind2[1]))
    current = base
    st = set()
    st.add(ind1)
    while True:
        temp = (current[0] - diff[0], current[1]- diff[1])
        if checkBounds(temp, board):
            st.add(temp)
        else:
            break
        current = temp
    # print(ind1, ind2, st)
    return st

def getAntinode(ind1, ind2):
    # print(ind1, ind2, (ind1[0] - (ind1[0] - ind2[0]) * 2, ind1[1] - 2 * (ind1[1] - ind2[1])))
    return (ind1[0] - (ind1[0] - ind2[0]) * 2, ind1[1] - 2 * (ind1[1] - ind2[1]))
    

def getUniqueLocations(charDict, board, pt1=True):
    st = set()
    for char, indices in charDict.items():
        for i1 in indices:
            for i2 in indices:
                if i1 == i2:
                    continue
                if not pt1:
                    a = getAntinodes(i1, i2, board)
                    st |= a
                    continue
                a = getAntinode(i1, i2)
                if checkBounds(a, board):
                    st.add(a)
    return len(st)
        

def firstPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    print(getUniqueLocations(makeDict(board), board))
    
def secondPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    print(getUniqueLocations(makeDict(board), board, pt1=False))
    

if __name__ == "__main__":
    # firstPart("input.txt")
    secondPart("input.txt")