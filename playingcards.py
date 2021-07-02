t = int(input())
for i in range(t):
    ta=input()
    ha=input().split()
    f = 0
    for j in range(len(ha)):
        if ta[0] == ha[j][0] or ta[1] == ha[j][1]:
           # print(ta[0],ha[j][0],ta[1],ha[j][1]) done in 20 min.:) :)
            f = 1
            break
        else:
            f = 0
    if f == 1:
        print("YES")
    else:
        print("NO")