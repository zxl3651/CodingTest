import sys
import math
from collections import deque


input = sys.stdin.readline

def put(n):
    global r
    if n == N:
        result.append(int(r))
        return
    for i, v in enumerate(op):
        if v > 0:
            ops = ''
            if i == 0:
                ops += '+'
            elif i == 1:
                ops += '-'
            elif i == 2:
                ops += '*'
            elif i == 3:
                ops += '/'
            op[i] -= 1
            tmp = r
            r = str(int(eval(r + ops + num[n])))
            put(n+1)
            r = tmp
            op[i] += 1

N = int(input())
num = list(input().split())
result = []
op = list(map(int, input().split()))
r = num[0]
cnt = 0
put(1)
print(max(result))
print(min(result))