
def getResult(numbers, comb):
    sm = numbers[0]
    for n in numbers[1:]:
        if comb % 2 == 0:
            sm += n
        else:
            sm *= n
        comb //= 2
    return sm

def checkPossible3(target, numbers):
    for comb in range(3**(len(numbers) - 1)):
        if getResult3(numbers, comb) == target:
            return target
    return 0

def getResult3(numbers, comb):
    sm = numbers[0]
    for n in numbers[1:]:
        if comb % 3 == 0:
            sm += n
        elif comb % 3 == 1:
            sm *= n
        else:
            sm = int(str(sm) + str(n))
        comb //= 3
    return sm

def checkPossible(target, numbers):
    for comb in range(2**(len(numbers) - 1)):
        if getResult(numbers, comb) == target:
            return target
    return 0
            
    
def firstPart(input):
    sm = 0
    cnt = 0
    with open(input) as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            print(cnt)
            cnt += 1
            sm += checkPossible(int(line.split(":")[0]), [int(i) for i in line.split(":")[1][1:].split(" ")])
    print(sm)
    
def secondPart(input):
    sm = 0
    cnt = 0
    with open(input) as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            print(cnt)
            cnt += 1
            sm += checkPossible3(int(line.split(":")[0]), [int(i) for i in line.split(":")[1][1:].split(" ")])
    print(sm)
    

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")