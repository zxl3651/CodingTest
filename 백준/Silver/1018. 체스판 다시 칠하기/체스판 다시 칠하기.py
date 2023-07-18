N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(input())
answer = []

for a in range(N-7):
    for b in range(M-7):
        w_index = 0
        b_index = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if chess[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        answer.append(w_index)
        answer.append(b_index)
print(min(answer))