from collections import deque

def solution(numbers, target):
    answer = 0
    result = deque([(0, 0)]) # deque((0, 0)) -> 대괄호를 빼고 선언하면 오류
    while result:
        s, n = result.popleft()
        if n > len(numbers) :
            break
        elif n == len(numbers) and s == target:
            answer += 1
        result.append((s+numbers[n-1], n+1))
        result.append((s-numbers[n-1], n+1))
    return answer