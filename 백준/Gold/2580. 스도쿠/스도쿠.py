import sys
import math
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def ckrow(x, a):
    for i in range(9):
        if arr[x][i] == a:
            return False
    return True
def ckcolumn(y, a):
    for i in range(9):
        if arr[i][y] == a:
            return False
    return True
def ckrec(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[nx + i][ny + j] == a:
                return False
    return True
def sudoku(idx):
    if idx == len(blank):
        for i in arr:
            for j in i:
                print(j, end=' ')
            print()
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if ckrow(x, i) and ckcolumn(y, i) and ckrec(x, y, i):
            arr[x][y] = i
            sudoku(idx + 1)
            arr[x][y] = 0

arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))
sudoku(0)