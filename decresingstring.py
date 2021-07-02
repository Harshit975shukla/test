t = int(input())
for i in range(t):
    s = input()
    a = [0] * 26
    b = [0] * 26
    for j in range(len(s)):
        a[ord(s[j]) - 97] += 1
    for j in range(25,-1,-1):
        print(chr(j+97) * a[j],end="")
    print("")
