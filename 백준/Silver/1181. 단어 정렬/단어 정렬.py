import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for i in range(N):
    arr.add(input()[:-1])
arr = sorted(list(arr), key=lambda x:x)
arr = sorted(arr, key=lambda x:len(x))
for i in arr:
    print(i)