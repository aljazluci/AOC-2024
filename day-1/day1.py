def firstPart(input):
    firstList = []
    secondList = []
    with open('input1.txt', 'r') as file:
        for line in file:
            l = line.split("   ")
            firstList.append(int(l[0]))
            secondList.append(int(l[1]))
    firstList.sort()
    secondList.sort()
    print(sum([abs(firstList[i] - secondList[i]) for i in range(len(firstList))]))

def secondPart(input):
    firstList = []
    secondList = []
    with open('input1.txt', 'r') as file:
        for line in file:
            l = line.split("   ")
            firstList.append(int(l[0]))
            secondList.append(int(l[1]))
    secondDict = dict()
    for s in secondList:
        if s not in secondDict:
            secondDict[s] = 1
            continue
        secondDict[s] += 1
        
    sum = 0
    for f in firstList:
        if f not in secondDict:
            continue
        sum += f * secondDict[f]
    print(sum)

if __name__ == "__main__":
    firstPart("input1.txt")
    secondPart("input1.txt")