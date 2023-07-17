s = input()
h = 0
b = 0
for i in range(len(s)):
    if i == 0:
        h += 10
        if s[i] == ')':
            b = 1
    else:
        if b == 1 and s[i] == '(':
            h += 10
            b = 0
        elif b == 0 and s[i] == ')':
            h += 10
            b = 1
        elif b == 1 and s[i] == ')':
            h += 5
        elif b == 0 and s[i] == '(':
            h += 5
print(h)