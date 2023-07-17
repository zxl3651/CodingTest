def solution(n):
    '''
    answer = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567
    '''
    dic = {0:0, 1:1}
    for i in range(n+1):
        if i not in dic:
            dic[i] = dic[i-1] + dic[i-2]
    return dic[n] % 1234567