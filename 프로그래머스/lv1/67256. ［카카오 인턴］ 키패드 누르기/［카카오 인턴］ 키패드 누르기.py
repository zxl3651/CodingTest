def solution(numbers, hand):
    answer = ''
    # 왼손 * 오른손 # 시작
    left = 10
    right = 12
    for n in numbers:
        if n == 0:
            n = 11
        if n % 3 == 1:
            answer += 'L'
            left = n
        elif n % 3 == 0:
            answer += 'R'
            right = n
        else:
            mL = abs(n - left)
            mR = abs(n - right)
            dL = (mL // 3) + (mL % 3)
            dR = (mR // 3) + (mR % 3)
            if dL > dR:
                answer += 'R'
                right = n
            elif dL < dR:
                answer += 'L'
                left = n
            else:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n
    print(answer)
    return answer