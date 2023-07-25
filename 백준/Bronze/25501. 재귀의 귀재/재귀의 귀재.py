import sys
from collections import deque

input = sys.stdin.readline

def recursion(s, l, r):
    global cnt
    if(l >= r):
        return 1
    elif(s[l] != s[r]):
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

T = int(input())
for i in range(T):
    cnt = 1
    s = input()[:-1]
    print(isPalindrome(s), cnt, sep=' ')