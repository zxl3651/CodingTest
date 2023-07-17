def solution(msg):
    answer = []
    dic = {'A':1, 'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    index = 0
    M = 27
    while(index < len(msg)):
        flag = 0
        w = msg[index]
        c = msg[index]
        while(index < len(msg)):
            if c in dic:
                w = c
                if index + 1 < len(msg):
                    index += 1
                    c += msg[index]
                else:
                    flag = 1
                    break
            else:
                break
        # 이부분 if flag: 없으면 통과안되는 이유 파악하기
        if flag:
            if index == len(msg) - 1:
                index += 1
        answer.append(dic[w])
        dic[c] = M #사전에 무조건 추가
        M += 1
    return answer