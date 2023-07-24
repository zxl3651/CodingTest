import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([i] for i in range(1, N+1))
for i in range(N-1):
    queue.popleft()
    n = queue.popleft()
    queue.append(n)
print(*queue.pop())