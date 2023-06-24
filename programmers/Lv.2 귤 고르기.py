from collections import Counter

def solution(k, tangerine):
    answer = 0
    dic = Counter(tangerine).most_common()
    num = 0
    for i in dic:
        tmp = num
        num += i[1]
        if num <= k:
            answer += 1
        elif tmp < k and num >= k:
            answer += 1
    return answer