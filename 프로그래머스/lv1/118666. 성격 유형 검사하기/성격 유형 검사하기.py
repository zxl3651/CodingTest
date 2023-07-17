def solution(survey, choices):
    answer = ''
    dicts = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: # choices 값이 4 미만일 시, survey의 앞의 값 출력
            dicts[survey[i][0]] += 4 - choices[i]

        elif choices[i] - 4 > 0: # choices 값이 4 초과 시, survey의 앞의 값 출력
            dicts[survey[i][1]] += choices[i] - 4

    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'

    return answer