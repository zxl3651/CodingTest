def solution(s, skip, index):
    answer = ''
    c = []
    # a = 97, z = 122
    for i in s:
        num = index
        n = 1
        a = ''
        while(num != 0):
            if ord(i) + n > 148:
                a = chr(ord(i) + n - 52)
            elif ord(i) + n > 122:
                a = chr(ord(i) + n - 26)
            else:
                a = chr(ord(i) + n)
            if a in skip:
                n += 1
            else:
                num -= 1
                n += 1
        answer += a
    return answer