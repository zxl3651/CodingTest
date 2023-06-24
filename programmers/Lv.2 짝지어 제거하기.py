def solution(s):
    answer = -1
    arr = []
    for i in s:
        if not arr: #arr이 list가 아니라면
            arr.append(i)
        elif arr[-1] == i: #글자가 짝이 맞는다면
            arr.pop()
        else: #글자가 짝이 맞지 않는다면
            arr.append(i)
    if not arr:
        return 1
    else:
        return 0