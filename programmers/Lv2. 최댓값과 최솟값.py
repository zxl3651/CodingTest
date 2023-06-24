def solution(s):
    num = list(map(int, s.split(' ')))
    a, b = str(min(num)), str(max(num))
    return a + ' ' + b
