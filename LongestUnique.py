s = list(input())
a = []
a3 = []
for j in range(len(s)):
    if s[j] not in a:
        a.append(s[j])
    # print("before", a)
    else:
        a3.append(len(a))
        #  print(a3)
        #  print("not in a", s[j])
        a.append(s[j])
        #   print("after adding element",a)
        y = a.index(s[j])
        y = y + 1
        #print(y)
        #  print(a)
        for k in range(y):
            x = a.pop(0)
               # print(x)
        #print("after adding and removing operation", a)
        a3.append(len(a))
print(max(a3))
# print(a3)
