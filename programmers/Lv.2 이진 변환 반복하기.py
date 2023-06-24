def solution(s):
    answer = []
    total = 0
    zero = 0
    while(s != '1'):
        total += 1
        num = s.count('1')
        zero += (len(s) - num) #남은 건 '0'의 개수
        s = bin(num)[2:]
    return [total, zero]