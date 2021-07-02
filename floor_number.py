t = int(input())
for i in range(t):
    n =int(input())
    arr = list(map(int, (input().split())))
    res = -1
    for j in range(n):
        if arr[j] == 1:
            res = j
    print(res)
