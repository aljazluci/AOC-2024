
def checkSafe(line, toRemove=0):
    if not line:
        return False
    list = [int(l) for l in line.split(" ")]
    return checkSafeList(list, toRemove=toRemove)
    

def checkSafeList(list, toRemove):
    if len(list) < 2:
        return True
    increasing = list[1] > list[0]
    if toRemove > 0:
            if checkSafeList(list[1:], toRemove-1):
                return True
    if list[1] == list[0]:
        if toRemove > 0:
            return checkSafeList(list[1:], toRemove-1)
        return False
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            if toRemove > 0:
                return checkSafeList(list[0:i] + list[i+1:], toRemove-1) or checkSafeList(list[0:i-1] + list[i:], toRemove-1) 
            return False
        if increasing != (list[i] > list[i-1]):
            if toRemove > 0:
                return checkSafeList(list[0:i] + list[i+1:], toRemove-1) or checkSafeList(list[0:i-1] + list[i:], toRemove-1) 
            return False
        if abs((list[i] - list[i-1])) > 3:
            if toRemove > 0:
                return checkSafeList(list[0:i] + list[i+1:], toRemove-1) or checkSafeList(list[0:i-1] + list[i:], toRemove-1) 
            return False
    
    return True
    

def firstPart(input):
    safeReports = 0
    with open(input, 'r') as file:
        for line in file:            
            safeReports += checkSafe(line)
            
    print(safeReports)
    
def secondPart(input):
    safeReports = 0
    with open(input, 'r') as file:
        for line in file:            
            safeReports += checkSafe(line, 1)
          
    print(safeReports)

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")