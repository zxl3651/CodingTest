import sys
import math
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
arr = []
answer = []

def check(a):
    tmp = sorted(a)
    if a != tmp:
        return False
    else:
        return True
def dfs():
    if len(arr) == M:
        if check(arr):
            print(' '.join(map(str, arr)))
        return
    else:
        for i in range(1, N+1):
            if i not in arr:
                arr.append(i)
                dfs()
                arr.pop()
dfs()