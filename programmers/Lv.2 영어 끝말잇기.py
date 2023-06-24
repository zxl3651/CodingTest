def solution(n, words):
    answer = [] #나온 단어 저장
    for i in range(len(words)):
        if not answer:
            answer.append(words[i])
        elif (answer[-1][-1] == words[i][0]) and (words[i] not in answer): #끝말잇기 규칙을 지켰는지 확인
            answer.append(words[i])
        else: #규칙을 지키지 않은 사람을 return
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0] #규칙을 다 지켰을 때 return