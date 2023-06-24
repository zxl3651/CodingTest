def solution(dirs):
    srcx, srcy, dirx, diry = 0, 0, 0, 0 #출발 x,y좌표, 도착 x,y좌표
    compare = []
    for i in dirs:
        if i == "L":
            if dirx == -5:
                continue
            else:
                dirx -= 1
        elif i == "R":
            if dirx == 5:
                continue
            else:
                dirx += 1
        elif i == "U":
            if diry == 5:
                continue
            else:
                diry += 1
        elif i == "D":
            if diry == -5:
                continue
            else:
                diry -= 1
        tmp = [srcx,srcy,dirx,diry] #모두 공통인 코드
        tmp2 = [dirx,diry,srcx,srcy]
        srcx, srcy = dirx, diry
        compare.append(tmp), compare.append(tmp2)
        
    arr = [] #중복 제거를 위한 리스트 선언
    for i in compare:
        if i not in arr:
            arr.append(i)
    return len(arr) // 2 #출발과 도착을 2개씩 넣었으므로 결과값 또한 2로 나누어야 한다.