import sys

input = sys.stdin.readline

def wave(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    if dp[n]:
        return dp[n]
    dp[n] = wave(n-2) + wave(n-3)
    return dp[n]

N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

dp = [0] * 101
dp[0], dp[1], dp[2] = 0, 0, 0
for i in P:
    print(wave(i))