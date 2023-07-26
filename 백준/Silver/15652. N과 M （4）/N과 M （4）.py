import sys
import math
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
    else:
        for i in range(start, N+1):
            arr.append(i)
            dfs(i)
            arr.pop()
dfs(1)