import sys
import math
from collections import deque
input = sys.stdin.readline

def star(n):
    if n == 1:
        return ['*'] 
    stars = star(n // 3)
    tmp = []
    for i in stars:
        tmp.append(i * 3)
    for i in stars:
        tmp.append(i + ' ' * (n//3) + i)
    for i in stars:
        tmp.append(i * 3)
    return tmp


N = int(input())
print('\n'.join(star(N)))