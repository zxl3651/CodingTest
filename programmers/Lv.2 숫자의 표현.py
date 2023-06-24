def solution(n):
    answer = 0
    num = 0
    index = 1
    while(num < n):
        if (n - (num)) % index == 0:
            answer += 1
        num += index
        index += 1
    return answer