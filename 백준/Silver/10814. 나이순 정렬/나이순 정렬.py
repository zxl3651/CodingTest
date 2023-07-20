import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for i in range(N):
    age, name = input().split()
    age = int(age)
    if age in dic:
        dic[age] += [name]
    else:
        dic[age] = [name]
dic = sorted(dic.items(), key=lambda x:x[0])
for i in dic:
    for j in i[1]:
        print(i[0], j)