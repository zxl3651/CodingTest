from collections import deque

def solution(priorities, location):
    answer = 0
    arr = deque(priorities)
    key1 = priorities[location]
    while(1):
        tmp1 = 0
        tmp2 = 0
        flag = False
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]: #만약 arr에 더 큰 수가 있을때 => 0번째를 맨 뒤에 집어넣는다.
                    tmp1 = arr.popleft()
                    arr.append(tmp1)
                    flag = True
                    if location == 0: #위치를 하나 줄여준다.
                        location = len(arr) - 1
                    else:
                        location -= 1
                    break
            if flag: #더 큰수가 있을 때 왼쪽껄 집어넣지 않고 다음으로 넘어간다.
                break
            else: #더 큰수가 없을 때 0번재를 pop 하고 answer을 증가시킨다.
                tmp2 = arr.popleft()
                answer += 1
                if location == 0:
                    return answer
                else:
                    location -= 1
                    break