n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum = 0
pre_time = 0

for time in arr:
  sum += (time + pre_time)
  pre_time += time

print(sum)
