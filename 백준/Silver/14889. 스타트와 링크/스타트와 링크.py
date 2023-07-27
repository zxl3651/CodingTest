import sys
import math
from collections import deque


input = sys.stdin.readline

def team(n, idx):

    if n == N//2:
        start_team, link_team = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_team += people[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += people[i][j]
        result.append(abs(start_team - link_team))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            team(n+1, i+1)
            visited[i] = False

N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int,input().split())))
result = []
visited = [False] * N
idx = 0
team(0,0)
print(min(result))