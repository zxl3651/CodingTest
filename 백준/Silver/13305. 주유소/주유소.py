n = int(input())
r = list(map(int, input().split()))
l = list(map(int, input().split()))
price = 0
i = 0
for i in range(0, len(r)-1):
  sum = 0
  if(i == 0):
    if(min(l) == l[i]):
      total = 0
      for j in r:
        total += j
      price += (total * l[i])
      break
    sum += r[i] * l[i]
  elif(l[i] <= l[i+1]):
    sum += (r[i] + r[i+1]) * l[i]
    i += 1
  else:
    sum += r[i] * l[i]
  price += sum
print(price)