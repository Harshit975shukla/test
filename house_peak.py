t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, (input().split())))
    res = -1
    #print(arr)
    for j in range(1, n - 1):
        if arr[j] > arr[j + 1] and arr[j] > arr[j - 1]:
            res = j
    if arr[0] > arr[1]:
        res = 0
    if arr[n - 1] > arr[n - 2]:
        res = n - 1
    print(res)
