def solution(n, m, section):
    answer = 0
    n = section[0]
    for i in section:
        if n-1 < i:
            n = (i + m - 1)
            answer += 1
    return answer