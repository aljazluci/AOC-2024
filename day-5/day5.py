def checkSorted(pageLine, rulesMap):
    for i in range(len(pageLine)):
        for j in range(i, len(pageLine)):
            if (pageLine[j], pageLine[i]) in rulesMap:
                return False
    return True
                

def firstPart(input):
    rules = []
    pages = []
    rulesFull = False
    with open(input, 'r') as file:
        for line in file:
            if line == "\n":
                rulesFull = True
                continue
            if rulesFull:
                if line[-1] == '\n':
                    line = line[:-1]
                pages.append([int(i) for i in line.split(',')])
                continue
            rules.append((int(line[:2]), int(line[3:5])))
    
    rulesMap = set()
    for r in rules:
        rulesMap.add(r)
    
    sm = 0
    for page in pages:
        if checkSorted(page, rulesMap):
            sm += page[len(page) // 2]
    print(sm)
    
def secondPart(input):
    rules = []
    pages = []
    rulesFull = False
    with open(input, 'r') as file:
        for line in file:
            if line == "\n":
                rulesFull = True
                continue
            if rulesFull:
                if line[-1] == '\n':
                    line = line[:-1]
                pages.append([int(i) for i in line.split(',')])
                continue
            rules.append((int(line[:2]), int(line[3:5])))
    
    rulesMap = set()
    for r in rules:
        rulesMap.add(r)
        
    sm = 0
    for page in pages:
        if not checkSorted(page, rulesMap):
            sm += rearrange(page, rulesMap)[len(page) // 2]
    print(sm)
        
def rearrange(pageLine, rulesMap):
    graph = set()
    for i in range(len(pageLine)):
        for j in range(i, len(pageLine)):
            if ((pageLine[i], pageLine[j]) in rulesMap):
                graph.add((pageLine[i],pageLine[j]))
            if ((pageLine[j], pageLine[i]) in rulesMap):
                graph.add((pageLine[j],pageLine[i]))
    # no, im not proud
    while not checkSorted(pageLine, rulesMap):
        for i in range(len(pageLine)):
            for j in range(i, len(pageLine)):
                if (pageLine[j], pageLine[i]) in graph:
                    temp = pageLine[i]
                    pageLine[i] = pageLine[j]
                    pageLine[j] = temp
    return pageLine

    
if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")