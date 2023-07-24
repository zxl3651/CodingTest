import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([i] for i in range(1, N+1))
answer = []
while(queue):
    queue.rotate(-K+1)
    n = queue.popleft()
    answer.append(str(*n))
print('<', ', '.join(answer), '>', sep='')