t = int(input())
f = 0
for i in range(t):
    s = input()
    dict = {}
    for j in s:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    for j in s:
        if dict[j] == 1:
            f = j
            break
        else:
            f = -1
    if f == -1:
        print(f)
    else:
      print(s.find(f))
