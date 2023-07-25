import sys
import math
from collections import deque
input = sys.stdin.readline

def cantoer(a):
    if len(a) == 1:
        return a
    else:
        l = len(a)
        start = l // 3
        start_s = '-' * start
        blank = ' ' * start
        return cantoer(start_s) + blank + cantoer(start_s)


while 1:
    try:
        N = int(input())
        arr = '-'* (3**N)
        arr = cantoer(arr)
        print(arr)
    except:
        break