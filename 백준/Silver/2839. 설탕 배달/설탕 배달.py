import math

N = int(input())

five, three = divmod(N,5)
if three % 3 == 0:
    print(five + (three//3))
else:
    s = 0
    while(N >= 3):
        s += 1
        N -= 3
        if N % 5 == 0:
            s += (N // 5)
            N %= 5
            break
    if N == 0:
        print(s)
    else:
        print(-1)