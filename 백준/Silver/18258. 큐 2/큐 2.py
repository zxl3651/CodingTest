import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(N):
    c = input().rstrip()
    if c == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif c == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == 'size':
        print(len(queue))
    elif c == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    else:
        c, n = c.split()
        queue.append(int(n))