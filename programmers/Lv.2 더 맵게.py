import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    flag = 0
    while(1):
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        n1 = heapq.heappop(scoville)
        if n1 >= K:
            break
        n2 = heapq.heappop(scoville)
        add = n1 + (n2 * 2)
        heapq.heappush(scoville, add)
        answer += 1
    return answer