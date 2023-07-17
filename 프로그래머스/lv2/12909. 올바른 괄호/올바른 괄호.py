def solution(s):
    arr1 = 0
    arr2 = 0
    for i in s:
        if i == '(':
            arr1 += 1
        elif i == ')':
            arr2 += 1
            if arr1 < arr2:
                return False
    if arr1 == arr2:
        return True
    else:
        return False