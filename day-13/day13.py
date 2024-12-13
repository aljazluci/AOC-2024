import math
import re
import numpy as np


def solve(x1, y1, x2, y2, xt, yt):
    mins = []
    for a in range(100):
        if a * x1 > xt or a * y1 > yt:
            break
        for b in range(100):
            if b * x2 > xt or b * y2 > yt:
                break
            if a * x1 + b * x2 == xt:
                if a * y1 + b * y2 == yt:
                    mins.append(3 * a + b)
    if not mins:
        return 0
    return min(mins)


def solveSecond(x1, y1, x2, y2, xt, yt):
    A = np.array([[x1, x2], [y1, y2]])
    B = np.array([xt, yt])
    B += 10000000000000
    if (x1 / x2) == (y1 / y2):
        print(x1, y1, x2, y2)
    if np.linalg.det(A) == 0:
        return 0
    X = np.linalg.inv(A) @ B 
    if abs(X[0] - round(X[0])) > 0.001:
        return 0
    if abs(X[1] - round(X[1])) > 0.001:
        return 0
    return round(X[0] * 3 + X[1])
    

def firstPart(input):
    arr = []
    with open(input) as file:
        for line in file: 
            if not line or line == '\n':
                continue
            arr.append([int(i) for i in re.findall("\d+", line)])
    sm = 0
    for i in range(len(arr) // 3):
        sm += solve(arr[i * 3+ 0][0], arr[i* 3 + 0][1], arr[i*3+ 1][0], arr[i*3+ 1][1], *arr[i*3 + 2])
    print(sm)
    
def secondPart(input):
    arr = []
    with open(input) as file:
        for line in file: 
            if not line or line == '\n':
                continue
            arr.append([int(i) for i in re.findall("\d+", line)])
    sm = 0
    for i in range(len(arr) // 3):
        sm += solveSecond(arr[i * 3+ 0][0], arr[i* 3 + 0][1], arr[i*3+ 1][0], arr[i*3+ 1][1], *arr[i*3 + 2])
    print(sm)

if __name__ == "__main__":
    firstPart("input.txt")
    secondPart("input.txt")