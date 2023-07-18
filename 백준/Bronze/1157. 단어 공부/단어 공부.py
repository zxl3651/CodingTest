from collections import Counter

N = Counter(input().upper()).most_common()
if len(N) == 1:
    print(N[0][0])
elif N[0][1] == N[1][1]:
    print('?')
else:
    print(N[0][0])