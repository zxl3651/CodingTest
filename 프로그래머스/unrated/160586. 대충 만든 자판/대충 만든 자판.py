def solution(keymap, targets):
    answer = []
    for i in targets: #target 각 원소 접근
        Sum = 0
        for j in i: #target 각 원소의 문자 하나 접근
            arr = []
            for k in keymap: #k번째 keymap에 접근
                if j in k:
                    arr.append(k.index(j) + 1) #해당하는 키의 인덱스 + 1
            if not arr: #해당 단어를 찾지 못했을때
                Sum = 0
                break
            else: #해당 단어를 찾았을 때 각 keymap의 원소 중 최소 인덱스 값을 합해줌
                Sum += min(arr)
        if Sum == 0: #만약 총 합이 0이면 찾지 못했으므로 -1을 넣어줌
            answer.append(-1)
        else:
            answer.append(Sum)
                
    return answer