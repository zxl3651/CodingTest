import sys
from math import factorial

input = sys.stdin.readline

N = int(input())
answer = []
bridge = []
for i in range(N):
    bridge.append(list(map(int, input().split())))
for i in bridge:
    n = i[0]
    m = i[1]
    answer.append(factorial(m) // (factorial(m-n) * factorial(n)))
for i in answer:
    print(i)