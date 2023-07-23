import sys
from math import factorial

input = sys.stdin.readline

N = int(input())
stack = []
answer = []
flag = 0
count = 1
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = 1
        break
if flag:
    print('NO')
else:
    for i in answer:
        print(i)