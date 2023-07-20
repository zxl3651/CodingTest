import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
answer = []
dic = {}
tmp = sorted(set(arr))
com = {}
for i in range(len(tmp)):
    com[tmp[i]] = i
for i in range(len(arr)):
    dic[arr[i]] = com[arr[i]]
for i in range(len(arr)):
    print(dic[arr[i]], end=' ')