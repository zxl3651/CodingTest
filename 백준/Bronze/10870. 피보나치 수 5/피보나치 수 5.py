import sys
from collections import deque

input = sys.stdin.readline

def fibo(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

N = int(input())
print(fibo(N))