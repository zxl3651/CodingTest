N = int(input())
A = {i:1 for i in list(map(int, (input().split())))}
M = int(input())
find = []
find = list((map(int, input().split())))
for i in find:
    if i in A:
        print(1)
    else:
        print(0)

