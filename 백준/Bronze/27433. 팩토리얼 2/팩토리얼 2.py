import sys
from collections import deque

input = sys.stdin.readline

def factorial(num):
    if num > 1:
        return factorial(num - 1) * num
    else:
        return 1


N = int(input())
print(factorial(N))