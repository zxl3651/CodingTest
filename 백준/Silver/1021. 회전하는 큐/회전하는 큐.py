import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int , input().split()))
queue = deque(i for i in range(1, N+1))
index = 0
cnt = 0
while index < len(arr):
    n = queue.popleft()
    if n == arr[index]:
        index += 1
        continue
    else:
        tmp = queue.index(arr[index])
        com = len(queue) // 2
        queue.appendleft(n)
        if tmp >= com:
            while queue[0] != arr[index]:
                queue.rotate(1)
                cnt += 1
        else:
            while queue[0] != arr[index]:
                queue.rotate(-1)
                cnt += 1
print(cnt)