import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    queue = deque(eval(input()))
    flag = 1
    rev = 0
    answer = []
    for i in p:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if rev:
                if queue:
                    flag = 1
                    queue.pop()
                else:
                    flag = 0
                    print('error')
                    break
            else:
                if queue:
                    flag = 1
                    queue.popleft()
                else:
                    flag = 0
                    print('error')
                    break
    if rev:
        queue.reverse()
    if queue or flag:
        for i in queue:
            answer.append(str(i))
        print('[', ','.join(answer),']', sep='')