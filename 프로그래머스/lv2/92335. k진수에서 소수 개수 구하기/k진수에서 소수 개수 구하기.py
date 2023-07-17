import math

def solution(n, k):
    answer = 0
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = rev_base[::-1]
    arr = rev_base.split("0")
    for N in arr:
        if N == '' or N == '1':
            continue
        n = int(N)
        flag = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                flag = 1
                break
        if not flag:
            answer += 1
    return answer