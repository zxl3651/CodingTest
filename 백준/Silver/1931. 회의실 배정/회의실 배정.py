n = int(input())
dic = []
for i in range(n):
  first, second = map(int, input().split())
  dic.append([first, second])
dic = sorted(dic, key= lambda a: a[0])
dic = sorted(dic, key= lambda a: a[1])
last = 0
sum = 0
for i,j in dic:
  if i >= last:
    sum += 1
    last = j
print(sum)
    