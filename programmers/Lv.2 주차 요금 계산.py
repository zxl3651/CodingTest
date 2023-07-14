import math

def solution(fees, records):
    answer = []
    dic = {}
    fee = {}
    for i in records:
        arr = i.split()
        if arr[2] == 'IN':
            dic[arr[1]] = arr[0]
        elif arr[2] == "OUT":
            H, M = map(int, arr[0].split(':'))
            h, m = map(int, dic[arr[1]].split(':'))
            M = (H * 60) + M
            m = (h * 60) + m
            time = M - m #time은 누적 주차 시간
            if arr[1] in fee:
                fee[arr[1]] += time
            else:
                fee[arr[1]] = time
            del dic[arr[1]]
            
            
    if dic:
        for i in dic:
            h, m = map(int, dic[i].split(':'))
            H, M = 23, 59
            m = (h * 60) + m
            M = (23 * 60) + 59
            time = M - m
            if i in fee:
                fee[i] += time
            else:
                fee[i] = time
    number = sorted(fee.keys())
    for i in number:
        time = fee[i]
        money = 0
        if time <= fees[0]: #기본 시간 여부 확인
            money = fees[1]
        elif time > fees[0]:
            money = (fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
        answer.append(money)
    return answer