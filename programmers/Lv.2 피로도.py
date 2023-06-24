from itertools import permutations

def solution(k, dungeons):
    arr = []
    for i in permutations(dungeons, len(dungeons)):
        arr.append(list(i))
    num = []
    for i in arr:
        cnt = 0
        n = k
        for j in i:
            if n >= j[0]:
                n -= j[1]
                cnt += 1
        num.append(cnt)
    return max(num)