def solution(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, b + a
    return a % 1234567