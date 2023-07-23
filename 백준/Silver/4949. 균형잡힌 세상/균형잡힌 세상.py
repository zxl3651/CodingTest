import sys
from math import factorial

input = sys.stdin.readline

string = []
while 1:
    c = input()[:-1]
    if c == ".":
        break
    else:
        string.append(c)
answer = []
for i in string:
    stack = []
    flag = 1
    for j in i:
        if j == ')':
            if not stack:
                answer.append('no')
                flag = 0
                break
            c = stack.pop()
            if c != '(':
                answer.append('no')
                flag = 0
                break
        elif j == ']':
            if not stack:
                answer.append('no')
                flag = 0
                break
            c = stack.pop()
            if c != '[':
                answer.append('no')
                flag = 0
                break
        elif j == '[' or j == '(':
            stack.append(j)
    if not stack and flag:
        answer.append('yes')
    elif stack and flag:
        answer.append('no')
for i in answer:
    print(i)