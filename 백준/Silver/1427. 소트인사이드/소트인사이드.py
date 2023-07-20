import sys
input = sys.stdin.readline

N = int(input())
arr = []
while(N > 10):
    n = N%10
    arr.append(n)
    N //= 10
arr.append(N)
arr = sorted(arr, reverse=True)
answer = ''
for i in arr:
    answer += str(i)
print(answer)