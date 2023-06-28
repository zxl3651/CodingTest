def solution(arr, k):
    answer = []
    for i in arr:
        if k % 2 == 1:
            i *= k
        else:
            i += k
        answer.append(i)
    return answer