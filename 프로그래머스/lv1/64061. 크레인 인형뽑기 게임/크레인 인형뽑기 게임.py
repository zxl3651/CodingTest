def solution(board, moves):
    answer = 0
    crane = [0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                n = crane[-1]
                if n == board[j][i-1]:
                    answer += 2
                    crane.pop()
                    board[j][i-1] = 0
                    break
                crane.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer