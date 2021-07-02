t = int(input())
for i in range(t):
    s = input()
    a = [0] * 26
    f = 0
    for j in s:
        a[ord(j)-97] += 1
    for j in range(26):
        if a[j] > 1:
            print("{}={}".format(chr(j+97) , a[j]),end=" ")
            f = 1
    if f == 0:
        print(-1)
    print("")