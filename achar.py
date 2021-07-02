t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    c = 0
    x = 0
    if l > 1:
        for j in s:
            if j == 'a':
                c += 1
    if c > (l // 2):
        x = l
    else:
        x = (c * 2 - 1)
        if x == 1:
            x = 0
    if l <= 1:
        x = 0
    if c == 1:
        x = 1
    print(x)
