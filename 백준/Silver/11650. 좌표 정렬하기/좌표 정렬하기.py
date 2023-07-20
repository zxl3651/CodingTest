import sys
input = sys.stdin.readline

N = int(input())
x = []
for i in range(N):
    num = list(map(int, input().split()))
    x.append(num)
arr = sorted(x, key=lambda x:x[0])
tmp = arr[0][0]
array = []
for i in arr:
    if tmp == i[0]:
        array.append(i)
    elif tmp != i[0]:
        array = sorted(array, key=lambda x: x[1])
        for j in array:
            print(j[0], j[1])
        array = []
        tmp = i[0]
        array.append(i)
for i in sorted(array, key=lambda x: x[1]):
    print(i[0], i[1])