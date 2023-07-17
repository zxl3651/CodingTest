def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        n1 = i // n
        n2 = i % n
        if n1 < n2: n1, n2 = n2, n1
        answer.append(n1 + 1)
    return answer