def solution(progresses, speeds):
    answer = []
    index = 0
    result = [0 for _ in range(len(speeds))]
    while(index != len(speeds)):
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
            
        for i in range(len(speeds)):
            if progresses[i] >= 100:
                result[i] = 1
                
        if result[index] == 1:
            n = index
            index += 1
            while(index != len(speeds)):
                if result[index] != 1:
                    break
                index += 1
            answer.append(index - n)
        
    return answer