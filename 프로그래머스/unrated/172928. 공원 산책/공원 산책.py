def solution(park, routes):
    start = [0,0]
    ob = []
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start[0] = i
                start[1] = j
            if park[i][j] == 'X':
                tmp = []
                tmp.append(i)
                tmp.append(j)
                ob.append(tmp)
    for i in routes:
        if i[0] == 'E':
            n = start[1]
            if n + int(i[2]) >= len(park[0]):
                continue
            else:
                for j in range(int(i[2])):
                    start[1] += 1
                    if start in ob:
                        start[1] = n
                        break
        if i[0] == 'W':
            n = start[1]
            if n - int(i[2]) < 0:
                continue
            else:
                for j in range(int(i[2])):
                    start[1] -= 1
                    if start in ob:
                        start[1] = n
                        break
        if i[0] == 'S':
            n = start[0]
            if n + int(i[2]) >= len(park):
                continue
            else:
                for j in range(int(i[2])):
                    start[0] += 1
                    if start in ob:
                        start[0] = n
                        break
        if i[0] == 'N':
            n = start[0]
            if n - int(i[2]) < 0:
                continue
            else:
                for j in range(int(i[2])):
                    start[0] -= 1
                    if start in ob:
                        start[0] = n
                        break
    return start