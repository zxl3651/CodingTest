def solution(num_list):
    num1 = 0
    num2 = 0
    for i in num_list:
        if num1 == 0:
            num1 = i
            num2 += i
            continue
        num1 *= i
        num2 += i
    if num1 < num2**2:
        return 1
    else:
        return 0