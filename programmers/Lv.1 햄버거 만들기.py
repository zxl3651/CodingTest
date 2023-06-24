def solution(ingredient):
    answer = 0
    a = 0
    for i in range(len(ingredient)):
        if ingredient[a:a+4] == [1,2,3,1]:
            del ingredient[a:a+4]
            answer += 1
            a -= 2
        else:
            a += 1
    return answer