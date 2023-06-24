def solution(cacheSize, cities):
    answer = 0
    stack = []
    
    for i in cities:
        i = i.lower()
        if i in stack:
            stack.remove(i)
            stack.append(i)
            answer += 1
        else:
            if cacheSize == 0: #cacheSize가 0일때
                answer += 5
                continue
            elif len(stack) >= cacheSize:
                stack.pop(0)
            stack.append(i)
            answer += 5
            
    return answer