def solution(dirs):
    answer = 0
    l, u = 0, 0
    c = [0,0]
    compare = []
    for i in dirs:
        if i == "L":
            if l == -5:
                continue
            else:
                l -= 1
                a, b = c[0], c[1]
                c[0] -= 1
                d, f = c[0], c[1]
                tmp = [a,b,d,f]
                tmp2 = [d,f,a,b]
                compare.append(list(tmp))
                compare.append(list(tmp2))
        elif i == "R":
            if l == 5:
                continue
            else:
                l += 1
                a, b = c[0], c[1]
                c[0] += 1
                d, f = c[0], c[1]
                tmp = [a,b,d,f]
                tmp2 = [d,f,a,b]
                compare.append(list(tmp))
                compare.append(list(tmp2))
        elif i == "U":
            if u == 5:
                continue
            else:
                u += 1
                a, b = c[0], c[1]
                c[1] += 1
                d, f = c[0], c[1]
                tmp = [a,b,d,f]
                tmp2 = [d,f,a,b]
                compare.append(list(tmp))
                compare.append(list(tmp2))
        elif i == "D":
            if u == -5:
                continue
            else:
                u -= 1
                a, b = c[0], c[1]
                c[1] -= 1
                d, f = c[0], c[1]
                tmp = [a,b,d,f]
                tmp2 = [d,f,a,b]
                compare.append(list(tmp))
                compare.append(list(tmp2))
    arr = []
    for i in compare:
        if i not in arr:
            arr.append(i)
    return len(arr) // 2