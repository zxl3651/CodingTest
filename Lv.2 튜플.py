from collections import Counter
def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    arr = s.split(',')
    count = Counter(arr).most_common()
    for i in count:
        answer.append(int(i[0]))
    return answer