def solution(record):
    answer = []
    result = []
    str1 = "님이 들어왔습니다."
    str2 = "님이 나갔습니다."
    dic = {}
    for i in record:
        arr = i.split()
        if arr[0] == "Enter":
            dic[arr[1]] = arr[2]
            answer.append(arr[1] + ' ' + str1)
        elif arr[0] == "Change":
            dic[arr[1]] = arr[2]
        elif arr[0] == "Leave":
            answer.append(arr[1] + ' ' + str2)
    for i in answer:
        Id = i.split()
        if Id[2] == "들어왔습니다.":
            result.append(dic[Id[0]] + str1)
        else:
            result.append(dic[Id[0]] + str2)
    return result