from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {i:0 for i in want}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    i = 0
    while(i+10 <= len(discount)):
        flag = True
        dis = discount[i:i+10]
        arr = Counter(dis)
        for j in range(len(dic)):
            if dic[want[j]] > arr[want[j]]:
                flag = False
                break
        if(flag):
            answer += 1
        i += 1
    return answer