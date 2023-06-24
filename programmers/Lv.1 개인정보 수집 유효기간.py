def solution(today, terms, privacies):
    answer = []
    Y,M,D = map(int, today.split('.')) #오늘 날짜 기록
    dic = {}
    
    for i in terms: # 약관 정보 기록
        a,b = i.split(' ')
        dic[a] = int(b)
        
    for i in range(len(privacies)):
        a, b = privacies[i].split(' ') #공백 기준 split
        y,m,d = map(int, a.split('.')) #날짜 split
        m += dic[b]
        
        while(1):
            if m > 12:
                y += 1
                m -= 12
            else:
                break
                
        d -= 1
        if d < 1:
            m -= 1
            d = 28
        #오늘 날짜와 약관의 유효기간을 더한 날짜를 비교
        if y < Y:
            answer.append(i+1)
        elif y == Y and m < M:
            answer.append(i+1)
        elif y == Y and m == M and d < D:
            answer.append(i+1)
            
    return answer