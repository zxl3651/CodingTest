import sys

input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(3)] for _ in range(N+1)]
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
for i in range(1, N+1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i-1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i-1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i-1][2]
print(min(dp[N]))