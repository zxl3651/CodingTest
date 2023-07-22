import sys
from math import factorial

input = sys.stdin.readline

k = int(input())
answer = []
for i in range(k):
    n = input()
    stack = []
    flag = 1
    for j in n[:-1]:
        if j == ')':
            if not stack:
                answer.append('NO')
                flag = 0
                break
            c = stack.pop()
            if c == ')':
                answer.append('NO')
                flag = 0
                break
        else:
            stack.append(j)
    if stack:
        answer.append('NO')
    elif flag:
        answer.append('YES')
for i in answer:
    print(i)