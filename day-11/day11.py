from functools import cache

@cache
def getFromNumber(number, stepsLeft):
    if stepsLeft == 0:
        return 1
    if number == 0:
        return getFromNumber(1, stepsLeft - 1)
    strnum = str(number)
    if len(strnum) % 2 == 0:
        return getFromNumber(int(strnum[:len(strnum) // 2]), stepsLeft - 1) + getFromNumber(int(strnum[len(strnum) // 2:]), stepsLeft - 1)
    return getFromNumber(number * 2024, stepsLeft - 1)


def firstPart(input):
    with open(input) as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            board = [int(i) for i in line.split(" ")]
    print(sum([getFromNumber(i, 25) for i in board]))
    
    
def secondPart(input):
    with open(input) as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            board = [int(i) for i in line.split(" ")]
    print(sum([getFromNumber(i, 75) for i in board]))
    

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")