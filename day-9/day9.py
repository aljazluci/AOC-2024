def getArray(board):
    arr = []
    curr = 0
    for i, b in enumerate(board):
        if i % 2 == 0:
            arr.extend([curr] * b)
        else:
            curr += 1
            arr.extend(['.']*b)
    return arr
            
def moveToBeg(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        if arr[start] != '.':
            start += 1
            continue
        if arr[end] == '.':
            end -= 1
            continue
        arr[start] = arr[end]
        arr[end] = '.'
        end -= 1
        start += 1
    return arr

def calc(arr):
    sm = 0
    for i, a in enumerate(arr):
        if a == '.':
            continue
        sm += a * i
    return sm
        
def findFirst(arr, size, limit):
    pointer = 0
    while True:
        if pointer >= limit:
            return -1
        if arr[pointer] == '.':
            for i in range(size):
                if pointer + i >= limit:
                    return -1
                if arr[pointer + i] != '.':
                    break
            else:
                return pointer
        pointer += 1
    
def findLast(arr, ind):
    if ind == 0:
        return -1, -1 ,-1
    cnt = 0
    while arr[ind] == '.':
        ind -= 1
    curr = arr[ind]
    while arr[ind] == curr:
        cnt += 1
        ind -=1
        if ind == -1:
            ind = 0
            break
    return ind + 1, cnt, arr[ind + 1]
    
def decrease(arr):
    end = len(arr) - 1
    for i in range(end, 0, -1):
        if arr[i] != '.':
            end = i
            break
    st = set()
    while True:
        ind, cnt, id = findLast(arr, end)
        if ind < 0:
            break
        if end <= 0:
            break
        newPos = findFirst(arr, cnt, ind)
        end = ind - 1
        if newPos < 0:
            continue
        if id in st:
            continue
        st.add(id)
        arr[newPos: newPos + cnt] = arr[ind: ind + cnt]
        arr[ind: ind + cnt] = ['.'] * cnt
    return arr 


def firstPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    board = [int(board[0][i]) for i in range(len(board[0]))]
    print(calc(moveToBeg(getArray(board))))
    
def secondPart(input):
    with open(input) as file:
        board = [list(line.strip()) for line in file]
    board = [int(board[0][i]) for i in range(len(board[0]))]
    arr = getArray(board)
    print(calc(decrease(getArray(board))))

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")