t = int(input())
for x in range(t):
    str1,str2 = input().split()
    m = len(str1)
    n = len(str2)
    j = 0
    i = 0
    while j < n and i < m:
        if str1[i] == str2[j]:
            i = i + 1
        j = j + 1
    if j == m:
        print("YES")
    else:
        print("NO")

