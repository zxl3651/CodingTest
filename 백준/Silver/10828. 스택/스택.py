import sys
from math import factorial

input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    c = input().rstrip()
    if c == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    else:
        c, n = c.split()
        stack.append(int(n))