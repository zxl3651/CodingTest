def solution(n):
    dic = {0:0, 1:1}
    for i in range(n+1):
        if i not in dic:
            dic[i] = dic[i-1] + dic[i-2]
    return dic[n] % 1234567