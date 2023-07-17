def solution(s):
    answer = 0
    while(1):
        x = 1
        X = 0
        n = 0
        if len(s) == 0:
            break
        c = s[0]
        for i in range(1, len(s)):
            if c == s[i]:
                x += 1
            elif c != s[i]:
                X += 1
            n = i
            if x == X:
                break
        answer += 1
        if n == len(s):
            break
        s = s[n+1:len(s)]
    return answer