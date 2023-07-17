def solution(n, t, m, p):
    answer = ''
    myturn = p
    dic = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
    for i in range(m*t):
        c = ''
        if i == 0:
            c = '0'
        else:
            while i > 0:
                i, a = divmod(i, n)
                c += dic[a]
        c = c[::-1]
        answer += c
    return "".join(answer[idx] for idx in range(p - 1, t * m, m))