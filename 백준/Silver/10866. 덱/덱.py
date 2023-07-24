import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(N):
    c = input().rstrip()
    if c == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif c == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == 'back':
        if queue:
            print(queue[-1])
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
        if c == 'push_front':
            queue.appendleft(int(n))
        else:
            queue.append(int(n))