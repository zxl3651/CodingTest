n, k = map(int, input().split())
arr = []
for i in range(n):
  arr.append(int(input()))
arr.reverse()

count = 0
i = 1

for coin in arr:
  count += k // coin
  k %= coin

print(count)