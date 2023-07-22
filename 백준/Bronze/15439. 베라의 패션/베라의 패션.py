import sys
input = sys.stdin.readline

N = int(input())
num = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            num += 1
print(num)