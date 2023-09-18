import sys

input = sys.stdin.readline

N = int(input())
A = {i:1 for i in map(int, input().split())}
M = int(input())
B = list(map(int, input().split()))
for i in B:
    if i in A:
        print("1")
    else:
        print("0")