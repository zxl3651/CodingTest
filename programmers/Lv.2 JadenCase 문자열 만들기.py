def solution(s):
    answer = ''
    s = s.split(" ")
    for i in s:
        if i == '':
            answer += ' '
        elif i[0].isalpha():
            answer += i[0].upper()
            answer += i[1:].lower()
            answer += ' '
        else:
            answer += i[0]
            answer += i[1:].lower()
            answer += ' '
    return answer[:-1]