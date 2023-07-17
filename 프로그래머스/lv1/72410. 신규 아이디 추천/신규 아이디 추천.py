def solution(new_id):
    answer = ''
    answer1 = new_id.lower() # 1단계
    answer2 = ''
    answer4 = ''
    answer5 = ''
    answer6 = ''
    for i in answer1: # 2단계
        n = 0
        if not i.isdigit():
            n += 1
        if not i.isalpha():
            n += 1
        if i not in ['-','_','.']:
            n += 1
        if n == 3:
            i = ''
        answer2 += i
    for i in range(len(answer2)-1 ,1, -1): # 3단계
        c = '.' * i
        if c in answer2:
            answer2 = answer2.replace(c, '.')
    
    answer4 = answer2.strip('.') # 4단계
    if not answer4: # 5단계
        answer4 += 'a'
    if len(answer4) >= 16: # 6단계
        answer4 = answer4[0:15].strip('.')
    while(len(answer4) <= 2): # 7단계
        answer4 += answer4[-1]
    return answer4