def solution(n):
    answer = 0
    num = n + 1
    while(1):
        if bin(num).count('1') == bin(n).count('1'):
            break
        num += 1
    return num