def solution(brown, yellow):
    answer = []
    x, y = 0, 0
    for i in range(1, yellow + 1):
        if yellow % i == 0: #yellow의 약수를 찾으면
            x = yellow // i
            y = i
            if x * 2 + y * 2 + 4 == brown: #yellow의 약수를 찾아도 조건이 충족되어야함
                return [x+2, y+2] #brown의 가로, 세로는 yellow의 가로, 세로보다 +2 길다.