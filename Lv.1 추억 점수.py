def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(yearning)):
        dic[name[i]] = yearning[i]
    for i in photo:
        n = 0
        for j in i:
            if j not in name:
                continue
            n += dic[j]
        answer.append(n)
    return answer