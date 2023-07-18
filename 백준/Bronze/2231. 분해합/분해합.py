N = int(input())
for i in range(1, N):
    n = sum(map(int, str(i)))
    cre = n + i
    if cre == N:
        print(i)
        break
else:
    print(0)