from collections import deque

def solution(s):
    deq = deque(s)
    answer = 0
    for i in range(len(s)):
        deq.rotate(-1)
        stack = []
        for j in deq:
            if not stack:
                stack.append(j)
            elif stack:
                if j == ')' and stack[-1] == '(':
                    stack.pop()
                elif j == '}' and stack[-1] == '{':
                    stack.pop()
                elif j == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(j)
        if not stack:
            answer += 1
                    
    return answer