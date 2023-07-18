N = int(input())

s = 0
while(N >= 0):
    if N % 5 == 0:
        s += (N // 5)
        print(s)
        break
    s += 1
    N -= 3
else:
    print(-1)