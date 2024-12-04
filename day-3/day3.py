import re

def multiply(mul):
    x1, x2 = mul[4:].split(",")
    x2 = x2[:-1]
    return int(x1) * int(x2)

def getMuls(line):
    return sum([multiply(i) for i in re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", line)])

def firstPart(input):
    mulSum = 0
    with open(input, 'r') as file:
        for line in file:
            mulSum += getMuls(line)
    print(mulSum)

def getMulsDos(line):
    return re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)|do\(\)|don't\(\)", line)

def getAll(instructions):
    do = True
    mulSum = 0
    for inst in instructions:
        if inst[0] == 'd':
            # do()
            do = inst[2] == '('
            continue
        if do:
            mulSum += multiply(inst)
    return mulSum
                
                

def secondPart(input):
    all = []
    with open(input, 'r') as file:
        for line in file:
            all.extend(getMulsDos(line))
    print(getAll(all))
            
if __name__ == "__main__":
    # firstPart("input.txt")
    secondPart("input.txt")