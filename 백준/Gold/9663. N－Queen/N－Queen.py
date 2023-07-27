import sys
import math
from collections import deque


input = sys.stdin.readline

def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
            return False
    return True
def nqueen(depth):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        if not visited[i]:
             board[depth] = i

             if check(depth):
                 visited[i] = True
                 nqueen(depth + 1)
                 visited[i] = False

N = int(input())

board = [0] * N
visited = [False] * N
result = 0
nqueen(0)
print(result)