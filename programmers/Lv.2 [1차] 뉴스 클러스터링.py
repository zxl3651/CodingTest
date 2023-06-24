def solution(str1, str2): #다중집합은 set()으로 표현할 수 없으니 list로 표현한다.
    answer = 0
    intersection = [] #교집합
    union = [] #합집합
    str3 = [] #str1을 두글자씩 끊은 리스트
    str4 = [] #str2를 두글자씩 끊은 리스트
    index = 0
    string = ''
    
    #str1과 str2를 두글자씩 끊기(조건에 맞춰서)
    for i in str1:
        if index == 1:
            string += i
            if not string.isalpha() or len(string.strip()) == 1:
                string = ''
            else:
                str3.append(string.lower())
                string = ''
            index = 0
        string += i
        index += 1
        
    index = 0
    string = ''
    
    for i in str2:
        if index == 1:
            string += i
            if not string.isalpha() or len(string.strip()) == 1:
                string = ''
            else:
                str4.append(string.lower())
                string = ''
            index = 0
        string += i
        index += 1
        
    arr1 = [] #길이가 긴 리스트
    arr2 = []
    if len(str3) >= len(str4):
        arr1,arr2 = str3, str4
    else:
        arr2,arr1 = str3, str4
        
    for i in arr1:
        if i in arr2:
            intersection.append(i)
            union.append(i)
            arr2.remove(i)
        elif not i in arr2:
            union.append(i)
            
    print(arr1, arr2)
    
    for i in arr2:
        #if not i in arr1: 이 한줄때문에 오류남..
            union.append(i)
    
    print(intersection, union)
    if not str3 and not str4: #둘다 공집합일때
        answer = 1
    else:
        answer = len(intersection) / len(union)
            
    return int(answer * 65536)