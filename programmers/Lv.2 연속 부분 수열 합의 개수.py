def solution(elements):
    answer = set()
    e = elements * 2
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(e[j:j+i+1]))
    return len(answer)