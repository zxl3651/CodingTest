def solution(n,a,b):
    answer = 1
    for i in range(n//2):
        if abs(a - b) == 1:
            n1 = 0
            n2 = 0
            if a % 2 != 0:
                n1 = a
                n2 = b
            else:
                n1 = b
                n2 = a
            if n1 + 1 == n2:
                return answer
            
        if a % 2 == 0:
            a //= 2
        else:
            a = (a // 2) + 1
        if b % 2 == 0:
            b //= 2
        else:
            b = (b // 2) + 1
        answer += 1
        
        