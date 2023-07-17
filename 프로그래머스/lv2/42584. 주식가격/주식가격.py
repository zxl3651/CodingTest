from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        n = queue.popleft()
        sec = 0
        for i in queue:
            sec += 1
            if n > i: # n이 i보다 크면 가격이 떨어졌다는 뜻
                break
        answer.append(sec)
    
    return answer