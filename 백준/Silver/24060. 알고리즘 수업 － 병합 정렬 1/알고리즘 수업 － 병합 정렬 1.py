import sys
import math
from collections import deque
input = sys.stdin.readline

def merge_sort(arr, p, r):
    if p < r:
        q = math.ceil((p+r) // 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr,p,q,r)
def merge(arr,p,q,r):
    global cnt, result
    i = p
    j = q+1
    tmp = []
    while(i<=q and j<= r):
        if(arr[i] <= arr[j]):
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while(i <= q):
        tmp.append(arr[i])
        i += 1
    while(j <= r):
        tmp.append(arr[j])
        j += 1
    i = p
    t = 0
    while(i<=r):
        arr[i] = tmp[t]
        cnt += 1
        if cnt == K:
            result = arr[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
result = -1
merge_sort(arr, 0, len(arr)-1)
print(result)