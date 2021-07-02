t = int(input())
for j in range(t):
    s = input()
    l = len(s)
    if l % 2 == 0:
        d = l // 2
    else:
        d = (l // 2) + 1
    a1 = s[0:d]
    a2 = s[-1:-d-1:-1]
    a2 = list(a2)
    s = 0
    for i in range(len(a1)):
        s = s + abs(ord(a1[i]) - ord(a2[i]))
    print(a1)
    print(a2)
    print(s)
