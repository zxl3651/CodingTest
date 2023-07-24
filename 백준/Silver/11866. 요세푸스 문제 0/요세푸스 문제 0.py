import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([i] for i in range(1, N+1))
answer = []
while(queue):
    queue.rotate(-K+1)
    n = queue.popleft()
    answer.append(*n)
print('<', end='')
for i in range(N-1):
    print(answer[i], end='')
    print(', ', end='')
print(answer[-1], end='')
print('>')