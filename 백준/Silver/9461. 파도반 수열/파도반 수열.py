import sys

input = sys.stdin.readline

T = int(input())
P = [0 for i in range(101)]
def fib(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif P[n]:
        return P[n]
    else:
        P[n] = fib(n-3) + fib(n-2)
        return P[n]

for i in range(T):
    print(fib(int(input())))
