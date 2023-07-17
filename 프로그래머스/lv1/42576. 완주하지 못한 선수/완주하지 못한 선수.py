def solution(participant, completion):
    answer = ''
    p = {i:0 for i in participant}
    for i in participant:
        p[i] += 1
    for i in completion:
        p[i] -= 1
    for i in p.keys():
        if p[i] == 1:
            answer += i
            break
    return answer