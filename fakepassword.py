t = int(input())
for i in range(t):
    o = input()
    f = input()
    lr = f[0:2]
    frl = f[2:len(f)]
    f1 = frl + lr
    rr = f[len(f)-2:len(f)]
    flr = f[0:len(f)-2]
    f2 = rr + flr
    if f2 == o or f1 == o:
        print("YES")
    else:
        print("NO")
  #  print(lr)
   # print(frl)
  #  print(f1)
  #  print(rr)
   # print(flr)
  #  print(f2)