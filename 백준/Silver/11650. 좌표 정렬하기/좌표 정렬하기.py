import sys
input = sys.stdin.readline

N = int(input())
x = []
for i in range(N):
    num = list(map(int, input().split()))
    x.append(num)
arr = sorted(x, key=lambda x:x[1])
arr = sorted(arr, key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])