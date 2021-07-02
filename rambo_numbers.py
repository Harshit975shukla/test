t = int(input())
for i in range(t):
    r,p,q=map(int,input().split())
    x = p // r
    y = q // r
    if p % r == 0:
        x = x - 1
    c = y - x
    print(c)