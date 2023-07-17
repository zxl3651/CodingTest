def solution(A,B):
    answer = 0
    A.sort(), B.sort() # 오름차순 정렬
    for i in range(len(A)):
        n = A[i] * B.pop()
        answer += n
    return answer