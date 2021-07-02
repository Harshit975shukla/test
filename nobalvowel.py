t = int(input())
for j in range(t):
    s = input()
    v = ['a', 'e', 'i', 'o', 'u']
    tmp = s[0]
    f = 1
    if len(s) > 1:
        for i in range(1, len(s)):
            #print(tmp,s[i])
            if tmp not in v and tmp != 'n':
                if s[i] not in v:
                    f = -1
                    break
                else:
                    f = 1
                    tmp = s[i]
            else:
                tmp = s[i]
        if s[i] not in v and s[i] != 'n':
            f = -1
        #print(f)
    else:
        if s in v or s == 'n':
            f = 1
        else:
            f = -1
    if f == 1:
        print("YES")
    else:
        print("NO")
