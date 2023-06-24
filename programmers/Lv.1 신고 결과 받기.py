def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {i:0 for i in id_list} #신고당한 횟수
    
    for i in set(report):
        ch = i.split(' ')
        dic[ch[1]] += 1 #신고당한 횟수 증가
        
    for i in set(report):
        ch = i.split(' ')
        if dic[ch[1]] >= k: #신고당한 횟수가 k 이상이라면
            answer[id_list.index(ch[0])] += 1 #id_list에서 ch[0]의 인덱스를 찾아 증가시켜줌(순서대로 하기위함)
    return answer