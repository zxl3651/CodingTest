import sys
import math
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N = int(input())

code1 = 1
code2 = 1

def fib(n):
    global code1
    if n == 1 or n == 2:
        return 1
    code1 += 1
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    global code2
    tmp = [0] * n
    tmp[1], tmp[2] = 1, 1
    for i in range(3, n):
        code2 += 1
        tmp[i] = tmp[i-1] + tmp[i-2]
    return tmp[n-1]

fib(N)
fibonacci(N)
print(code1, code2, sep=' ')