def solution(citations):
    citations.sort(reverse = True)
    print(citations)
    Max = citations[0]
    while(1): #코드 시간을 줄여보자!
        arr = []
        for i in citations:
            if Max <= i:
                arr.append(i)
        if Max <= len(arr):
            return Max
        Max -= 1