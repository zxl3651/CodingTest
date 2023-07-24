import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
answer = []
for i in range(num):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))
    top = max(arr)
    index = 1
    while arr:
        n = arr.popleft()
        if n >= top:
            if M == 0:
                answer.append(index)
                break
            top = max(arr)
            index += 1
            M -= 1
        else:
            arr.append(n)
            if M == 0:
                M = len(arr)-1
            else:
                M -= 1
for i in answer:
    print(i)