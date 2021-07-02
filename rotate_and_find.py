t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    if x not in arr:
        res = -1
    else:
        res = arr.index(x)
    print(res)
