def solution(s):
    answer = -1
    arr = []
    for i in s:
        if not arr:
            arr.append(i)
        elif arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)
    if not arr:
        return 1
    else:
        return 0