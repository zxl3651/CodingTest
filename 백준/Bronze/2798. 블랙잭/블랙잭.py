N, M = map(int, input().split())
deck = list(map(int, input().split()))
m = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            n = deck[i] + deck[j] + deck[k]
            if n <= M and m < n:
                m = n
print(m)